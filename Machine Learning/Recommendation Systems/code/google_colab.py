from urllib.request import urlretrieve
import zipfile
import pandas as pd
import google_colab_helper as h


# region Get MovieLens Data
urlretrieve("http://files.grouplens.org/datasets/movielens/ml-100k.zip", "movielens.zip")
zip_ref = zipfile.ZipFile('movielens.zip', 'r')
zip_ref.extractall()
# endregion

# region Load dataset
users_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=users_cols, encoding='latin-1')

ratings_col = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=ratings_col, encoding='latin-1')

genre_cols = [
    "genre_unknown", "Action", "Adventure", "Animation", "Children", "Comedy",
    "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror",
    "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
]
movies_cols = ['movie_id', 'title', 'release_date', "video_release_date", "imdb_url"] + genre_cols
movies = pd.read_csv('ml-100k/u.item', sep='|', names=movies_cols, encoding='latin-1')

users["user_id"] = users["user_id"].apply(lambda x: str(x - 1))
movies["movie_id"] = movies["movie_id"].apply(lambda x: str(x - 1))
movies["year"] = movies['release_date'].apply(lambda x: str(x).split('-')[-1])
ratings["movie_id"] = ratings["movie_id"].apply(lambda x: str(x - 1))
ratings["user_id"] = ratings["user_id"].apply(lambda x: str(x - 1))
ratings["rating"] = ratings["rating"].apply(lambda x: float(x))
# endregion

# region PreProcessing
pd.DataFrame.mask = h.mask
pd.DataFrame.flatten_cols = h.flatten_cols
genre_occurances = movies[genre_cols].sum().to_dict()
movies = h.mark_genres(movies, genre_cols)

movielens = ratings \
    .merge(movies, on='movie_id') \
    .merge(users, on='user_id')

users_ratings = ratings.groupby('user_id', as_index=False) \
    .agg({'rating': ['count', 'mean']}) \
    .flatten_cols() \
    .merge(users, on='user_id')

movies_ratings = movies \
    .merge(ratings
            .groupby('movie_id', as_index=False)
            .agg({'rating': ['count', 'mean']})
            .flatten_cols(), on='movie_id')

# endregion

# region Train Model
"""
model = h.build_model(ratings,
                      num_users=len(users), num_movies=len(movies),
                      embedding_dim=30, init_stddev=0.5)
model.train(num_iterations=1000, learning_rate=10., plot_results=False)
"""

reg_model = h.build_regularized_model(ratings,
                                      num_users=len(users), num_movies=len(movies),
                                      embedding_dim=35, regularization_coeff=0.1, gravity_coeff=1.,
                                      init_stddev=.05)
reg_model.train(num_iterations=2000, learning_rate=20., plot_results=True)
# endregion

# region Query Model, Visualize
reco = h.user_recommendations(reg_model, 5, movies, ratings, measure='cosine')
neigh = h.movie_neighbors(reg_model, movies, "Aladdin", measure='cosine')
movies = h.tsne_movie_embeddings(reg_model, movies)
# endregion
