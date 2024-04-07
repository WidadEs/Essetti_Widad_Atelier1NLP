import re
from pymongo import MongoClient
import nltk

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['scrapy_db']
collection = db['articles']

# Télécharger les données nltk nécessaires
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')


def rule_based_pos_tagging_arabic(text):
    # Tokeniser le texte en phrases
    sentences = nltk.sent_tokenize(text)

    pos_tags = []
    for sentence in sentences:
        # Tokeniser chaque phrase en mots
        words = nltk.word_tokenize(sentence)

        # Taguer chaque mot avec un POS tag
        tagged_words = nltk.pos_tag(words)

        # Ajouter les POS tags tagués à la liste
        pos_tags.extend(tagged_words)

    return pos_tags


# Appliquer le POS tagging basé sur des règles à chaque document
for doc in collection.find():
    article_text = doc['text']
    pos_tags = rule_based_pos_tagging_arabic(article_text)

    # Mettre à jour le document dans la collection avec les POS tags
    collection.update_one({'_id': doc['_id']}, {
        '$set': {
            'pos_tags': pos_tags
        }
    })
