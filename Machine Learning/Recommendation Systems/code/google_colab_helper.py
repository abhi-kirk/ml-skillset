import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import tensorflow.compat.v1 as tf
from google_colab_cfmodel import CFModel


tf.disable_eager_execution()


def mask(df, key, function):
    return df[function(df[key])]


def flatten_cols(df):
    df.columns = [' '.join(col).strip() for col in df.columns.values]
    return df


def split_dataframe(df, holdout_fraction=0.1):
    test = df.sample(frac=holdout_fraction, replace=False)
    train = df[~df.index.isin(test.index)]
    return train, test


def mark_genres(movies, genres):
    def get_random_genre(gs):
        active = [genre for genre, g in zip(genres, gs) if g == 1]
        if len(active) == 0:
            return 'Other'
        return np.random.choice(active)

    def get_all_genres(gs):
        active = [genre for genre, g in zip(genres, gs) if g == 1]
        if len(active) == 0:
            return 'Other'
        return '-'.join(active)

    movies['genre'] = [
        get_random_genre(gs) for gs in zip(*[movies[genre] for genre in genres])]
    movies['all_genres'] = [
        get_all_genres(gs) for gs in zip(*[movies[genre] for genre in genres])]
    return movies


def build_rating_sparse_tensor(ratings_df, num_users, num_movies):
    indices = ratings_df[['user_id', 'movie_id']].values
    values = ratings_df['rating'].values
    return tf.SparseTensor(
        indices=indices,
        values=values,
        dense_shape=[num_users, num_movies]
    )


def sparse_mean_square_error(sparse_ratings, user_embeddings, movie_embeddings):
    predictions = tf.gather_nd(
        params=tf.matmul(user_embeddings, movie_embeddings, transpose_b=True),
        indices=sparse_ratings.indices
    )
    predictions_opt = tf.reduce_sum(
        tf.gather(user_embeddings, sparse_ratings.indices[:, 0]) *
        tf.gather(movie_embeddings, sparse_ratings.indices[:, 1]),
        axis=1
    )
    loss = tf.losses.mean_squared_error(sparse_ratings.values, predictions)
    return loss


def build_model(ratings, num_users, num_movies, embedding_dim=3, init_stddev=1.):
    n, m = num_users, num_movies
    train_ratings, test_ratings = split_dataframe(ratings)
    A_train = build_rating_sparse_tensor(train_ratings, n, m)
    A_test = build_rating_sparse_tensor(test_ratings, n, m)
    U = tf.Variable(tf.random.normal(
        [A_train.dense_shape[0], embedding_dim],
        stddev=init_stddev
    ))
    V = tf.Variable(tf.random.normal(
        [A_test.dense_shape[1], embedding_dim],
        stddev=init_stddev
    ))
    train_loss = sparse_mean_square_error(A_train, U, V)
    test_loss = sparse_mean_square_error(A_test, U, V)
    metrics = {
        'train_error': train_loss,
        'test_error': test_loss
    }
    embeddings = {
        'user_id': U,
        'movie_id': V
    }
    return CFModel(embeddings, train_loss, [metrics])


def compute_scores(query_embedding, item_embeddings, measure='dot'):
    u, V = query_embedding, item_embeddings
    if measure == 'cosine':
        V /= np.linalg.norm(V, axis=1, keepdims=True)
        u /= np.linalg.norm(u)
    return u.dot(V.T)


def user_recommendations(model, user_id, movies, ratings, measure='dot', exclude_rated=False, k=6):
    scores = compute_scores(model.embeddings['user_id'][user_id], model.embeddings['movie_id'], measure)
    score_key = measure + ' score'
    df = pd.DataFrame({
        score_key: list(scores),
        'movie_id': movies['movie_id'],
        'titles': movies['title'],
        'genres': movies['all_genres']
    })
    if exclude_rated:
        rated_movies = ratings[ratings.user_id == str(user_id)]['movie_id'].values
        df = df[df.movie_id.apply(lambda movie_id: movie_id not in rated_movies)]
    return df.sort_values([score_key], ascending=False).head(k)


def movie_neighbors(model, movies, title_substring, measure='dot', k=6):
    ids = movies[movies['title'].str.contains(title_substring)].index.values
    titles = movies.iloc[ids]['title'].values
    if len(titles) == 0:
        raise ValueError("Found no movies with title %s" % title_substring)
    print("Nearest Neighbors of : %s." % titles[0])
    if len(titles) > 1:
        print("[Found more than one matching movie. Other candidates: {}]".format(
            ", ".join(titles[1:])
        ))
    movie_id = ids[0]
    scores = compute_scores(
        model.embeddings['movie_id'][movie_id],
        model.embeddings['movie_id'],
        measure
    )
    score_key = measure + ' score'
    df = pd.DataFrame({
        score_key: list(scores),
        'titles': movies['title'],
        'genres': movies['all_genres']
    })
    return df.sort_values([score_key], ascending=False).head(k)


def gravity(U, V):
    return 1. / (U.shape[0] * V.shape[0]) * tf.reduce_sum(
        tf.matmul(U, U, transpose_a=True) * tf.matmul(V, V, transpose_a=True)
    )


def build_regularized_model(ratings, num_users, num_movies,
                            embedding_dim=3, regularization_coeff=.1, gravity_coeff=1., init_stddev=.1):
    n, m = num_users, num_movies
    train_ratings, test_ratings = split_dataframe(ratings)
    A_train = build_rating_sparse_tensor(train_ratings, n, m)
    A_test = build_rating_sparse_tensor(test_ratings, n, m)
    U = tf.Variable(tf.random_normal(
        [A_train.dense_shape[0], embedding_dim], stddev=init_stddev))
    V = tf.Variable(tf.random_normal(
        [A_train.dense_shape[1], embedding_dim], stddev=init_stddev))
    error_train = sparse_mean_square_error(A_train, U, V)
    error_test = sparse_mean_square_error(A_test, U, V)
    gravity_loss = gravity_coeff * gravity(U, V)
    regularization_loss = regularization_coeff * (
            tf.reduce_sum(U * U) / U.shape[0] + tf.reduce_sum(V * V) / V.shape[0])
    total_loss = error_train + regularization_loss + gravity_loss
    losses = {
        'train_error_observed': error_train,
        'test_error_observed': error_test,
    }
    loss_components = {
        'observed_loss': error_train,
        'regularization_loss': regularization_loss,
        'gravity_loss': gravity_loss,
    }
    embeddings = {"user_id": U, "movie_id": V}
    return CFModel(embeddings, total_loss, [losses, loss_components])


def tsne_movie_embeddings(model, movies):
    tsne = TSNE(
        n_components=2, perplexity=40, metric='cosine', early_exaggeration=10.,
        init='pca', verbose=True, n_iter=400
    )
    print("Running t-SNE...")
    V_proj = tsne.fit_transform(model.embeddings["movie_id"])
    movies.loc[:, 'x'] = V_proj[:, 0]
    movies.loc[:, 'y'] = V_proj[:, 1]
    return movies


def visualize_movie_embeddings(data, x, y):
    pass
