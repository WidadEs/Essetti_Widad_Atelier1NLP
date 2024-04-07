# Essetti_Widad_Atelier1NLP
## 1-Efficient Data Extraction  from CNN Arabic World News Using Scrapy and beautifulsoup
For data scraping from the CNN Arabic World News website, I utilize a combination of Scrapy and Beautiful Soup. Scrapy serves as the main framework for web crawling and scraping, handling the systematic retrieval of web pages and content. It streamlines the extraction process by automating HTTP requests, managing response parsing, and facilitating structured data extraction using customizable XPath or CSS selectors. However, Scrapy's strength lies in its ability to navigate websites and fetch content efficiently.
On the other hand, Beautiful Soup complements Scrapy by providing robust HTML parsing capabilities. It excels at handling complex HTML structures, extracting specific elements like article text, titles, and URLs with ease. By combining Scrapy's web crawling prowess with Beautiful Soup's parsing flexibility, I can effectively extract targeted data from the CNN Arabic World News pages. This hybrid approach ensures accuracy, completeness, and adaptability, enabling me to gather the desired information for further analysis and storage in MongoDB.
## 2-Storage in MongoDB
To store the extracted data effectively, I utilize MongoDB, a NoSQL database known for its flexibility and scalability. MongoDB allows me to store data in JSON-like documents, making it suitable for unstructured and semi-structured data like news articles. With MongoDB, I can easily insert, update, and query data, ensuring efficient data management and retrieval for future analysis and applications.
## 3-Establishment of NLP Pipeline (Text Cleaning, Tokenization, Stop words, Discretization,Normalization)
### 3.1 MongoDB Connection Setup
Establishes a connection to MongoDB to interact with the 'scrapy_db' database and the 'articles' collection.
### 3.2 Stopwords Download
Downloads Arabic stopwords from NLTK's corpus, which are later used for text preprocessing.
### 3.3 Text Cleaning
Utilizes regular expressions (regex) to clean the text by removing special characters and multiple spaces, focusing on Arabic characters.
### 3.4 Text Tokenization
Tokenizes the cleaned text into words and sentences using NLTK's word_tokenize and sent_tokenize functions.
### 3.5 Stopwords Removal
Removes stopwords from the tokenized words using NLTK's Arabic stopwords list to filter out common and irrelevant words.
### 3.6 Text Vectorization (TF-IDF)
Utilizes Scikit-Learn's TfidfVectorizer to convert the preprocessed text into a numerical representation using TF-IDF (Term Frequency-Inverse Document Frequency).
The TF-IDF vectorizer is configured to handle Arabic text and creates a sparse matrix of vectorized text data.
### 3.7 NLP Pipeline Execution
Iterates through each document in the MongoDB collection.
Performs the entire NLP pipeline, including text cleaning, tokenization, stopwords removal, stemming, and TF-IDF vectorization, on the article text.
Updates each document in the collection with the results of the NLP pipeline, including cleaned text, tokenized words, sentences, filtered words, vectorized text, and stemmed words.
## 4-Do the Stemming and Lemmatization, then compare the tow mechanisms.
### 4.1-Text Stemming
Stems the filtered words using the SnowballStemmer from NLTK with the Arabic language support, reducing words to their base or root form.
### 4.2-Text Lemmatization
The lemmatize_text function is used for lemmatization, a process in natural language processing (NLP) that aims to reduce words to their base or root form. In this function, the WordNetLemmatizer from NLTK is utilized to perform lemmatization on a list of words. Each word in the input list is lemmatized using the lemmatize method provided by the WordNetLemmatizer, resulting in a list of lemmatized words. Lemmatization is commonly employed in text preprocessing tasks to standardize word forms and improve the accuracy of downstream NLP applications such as text classification, information retrieval, and sentiment analysis.
### 4.3 comparison
stemming is a faster and less accurate method that may result in non-words but is suitable for tasks prioritizing efficiency and where minor word variations are acceptable. On the other hand, lemmatization is a more accurate method that produces valid words but requires more computational resources and is slower, making it ideal for tasks requiring precise word meanings and linguistic accuracy.
## 5-Apply Parts of Speech technics based on both Rule based and Machine learning approaches.
The process begins by establishing a connection to the MongoDB instance and downloading essential NLTK packages for tokenization and POS tagging. The core functionality lies in the rule_based_pos_tagging_arabic function, which tokenizes text into sentences and further tokenizes each sentence into words. Through NLTK's pos_tag function, it assigns POS tags to each word based on predefined linguistic rules. The script iterates through documents in the MongoDB collection, applies the POS tagging function to each document's text, and stores the generated POS tags back into the collection. This automated process streamlines the extraction of linguistic information, aiding in tasks such as text analysis, information retrieval, and natural language processing applications.
## 6-Apply NER Methods.
It begins by establishing a connection to the MongoDB instance and downloading the Arabic model for Stanza, enabling the processing of Arabic text. The core function stanza_ner processes the text using Stanza's NER pipeline, which identifies named entities and their corresponding labels within the text. The script iterates through documents in the MongoDB collection, applies the NER function to each document's text, and stores the extracted named entities along with their labels back into the collection. This streamlined approach enhances the efficiency of extracting structured information such as person names, locations, and organizations, contributing to tasks like information retrieval, text categorization, and semantic analysis in natural language processing applications.
