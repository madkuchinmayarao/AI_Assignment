import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample text data
text_data = """
Natural language processing (NLP) is a subfield of artificial intelligence concerned with the interaction 
between computers and humans using natural language. The ultimate objective of NLP is to enable computers 
to understand, interpret, and generate human language in a way that is both valuable and meaningful.
"""

def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return filtered_tokens

def lemmatize_text(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

def stem_text(tokens):
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

def main():
    # Tokenization
    tokens = tokenize_text(text_data)
    print("Tokenized Text:")
    print(tokens)

    # Stopword Removal
    tokens_without_stopwords = remove_stopwords(tokens)
    print("\nText after Stopword Removal:")
    print(tokens_without_stopwords)

    # Lemmatization
    lemmatized_tokens = lemmatize_text(tokens_without_stopwords)
    print("\nText after Lemmatization:")
    print(lemmatized_tokens)

    # Stemming
    stemmed_tokens = stem_text(tokens_without_stopwords)
    print("\nText after Stemming:")
    print(stemmed_tokens)

if __name__ == "__main__":
    main()
