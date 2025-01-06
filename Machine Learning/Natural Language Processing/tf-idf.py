import numpy as np

# Corpus
corpus = [
    "cat sat on the mat",
    "dog sat on the mat",
    "cat and dog sat"
]

# Sentence for which we want to calculate the TF-IDF
sentence = "cat sat on the mat"

# Step 1: Tokenize the Corpus
def tokenize(text):
    return text.lower().split()

# Tokenized corpus
tokenized_corpus = [tokenize(doc) for doc in corpus]
vocabulary = sorted(set(word for doc in tokenized_corpus for word in doc))
vocab_index = {word: idx for idx, word in enumerate(vocabulary)}

print("Vocabulary:", vocabulary)

# Step 2: Compute Term Frequency (TF)
def compute_tf(tokens, vocab_index):
    tf = np.zeros(len(vocab_index))
    for word in tokens:
        if word in vocab_index:
            tf[vocab_index[word]] += 1
    return tf / len(tokens)

# Step 3: Compute Inverse Document Frequency (IDF)
def compute_idf(tokenized_corpus, vocab_index):
    doc_count = len(tokenized_corpus)
    idf = np.zeros(len(vocab_index))
    for word, idx in vocab_index.items():
        containing_docs = sum(1 for doc in tokenized_corpus if word in doc)
        idf[idx] = np.log((doc_count / (1 + containing_docs))) + 1  # Adding 1 to avoid division by zero
    return idf

# Step 4: Compute TF-IDF for the Sentence
def compute_tfidf(sentence, tokenized_corpus, vocab_index):
    idf = compute_idf(tokenized_corpus, vocab_index)
    tokens = tokenize(sentence)
    tf = compute_tf(tokens, vocab_index)
    tfidf = tf * idf
    return tfidf

# Calculate TF-IDF
tfidf_vector = compute_tfidf(sentence, tokenized_corpus, vocab_index)
print("\nTF-IDF Vector for the Sentence:")
print(tfidf_vector)

# Optional: Display as a dictionary
tfidf_dict = {word: tfidf_vector[idx] for word, idx in vocab_index.items()}
print("\nTF-IDF Vector as Dictionary:")
print(tfidf_dict)
