import re
from pymongo import MongoClient
import stanza

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['scrapy_db']
collection = db['articles']

# Télécharger le modèle arabe de Stanza
stanza.download('ar')

# Initialiser Stanza pour l'arabe
nlp = stanza.Pipeline(lang='ar', processors='tokenize,ner')

def stanza_ner(text):
    # Traiter le texte avec Stanza
    doc = nlp(text)

    # Extraire les entités nommées et leurs étiquettes
    named_entities = []
    for sentence in doc.sentences:
        for entity in sentence.ents:
            named_entities.append((entity.text, entity.type))

    return named_entities

# Appliquer la NER avec Stanza à chaque document
for doc in collection.find():
    article_text = doc['text']
    ner_tags = stanza_ner(article_text)

    # Mettre à jour le document dans la collection avec les NER tags
    collection.update_one({'_id': doc['_id']}, {
        '$set': {
            'ner_tags': str(ner_tags)
        }
    })
