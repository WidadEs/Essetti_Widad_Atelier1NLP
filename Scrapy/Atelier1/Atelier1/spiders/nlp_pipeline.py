from pymongo import MongoClient
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['scrapy_db']
collection = db['articles']

import nltk
nltk.download('wordnet')
# Download Arabic stopwords
nltk.download('stopwords')


def clean_text(text):
    # Remove special characters and multiple spaces
    cleaned_text = re.sub(r'[^\u0621-\u064A\s]', '', text)  # Arabic characters
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()


def tokenize_text(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    return words, sentences


def remove_stopwords(words):
    stop_words = set(stopwords.words('arabic'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words


def stem_text(words):
    stemmer = SnowballStemmer("arabic")
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words


def lemmatize_text(words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return lemmatized_words


import numpy as np


def vectorize_text(texts, method='tfidf'):
    # Create an instance of the TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Concatenate filtered words into a string for each text
    text_str = [' '.join(words) for words in texts]

    # Check if the text contains words
    if any(text_str):
        # Vectorize concatenated texts
        vectorized_text = vectorizer.fit_transform(text_str)

        # Convert the sparse matrix into a NumPy array
        dense_matrix = vectorized_text.toarray()

        # Convert the NumPy array into a list of lists
        dense_matrix_list = dense_matrix.tolist()

        return dense_matrix_list
    else:
        return None


def apply_nlp_pipeline():
    for doc in collection.find():
        article_text = doc['text']
        cleaned_text = clean_text(article_text)
        words, sentences = tokenize_text(cleaned_text)
        filtered_words = remove_stopwords(words)
        stemmed_words = stem_text(filtered_words)
        lemmatized_words = lemmatize_text(filtered_words)
        vectorized_text = vectorize_text([filtered_words], method='tfidf')

        # Update the document in the collection with the NLP pipeline results
        collection.update_one({'_id': doc['_id']}, {
            '$set': {
                'cleaned_text': cleaned_text,
                'tokenized_words': words,
                'sentences': sentences,
                'filtered_words': filtered_words,
                'stemmed_words': stemmed_words,
                'lemmatized_words': lemmatized_words,
                'vectorized_text': vectorized_text,
            }
        })


# Execute the NLP pipeline
apply_nlp_pipeline()
