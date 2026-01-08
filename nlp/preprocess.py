import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Tell nltk where your data folder is
nltk.data.path.append("nltk_data")

# Initialize tools
stop_words = set(stopwords.words("english"))
custom_stopwords = {
    "please", "plz", "plzz", "pls", "u", "me", "on", "off", "'s"
}
stop_words = stop_words.union(custom_stopwords)

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()                           # lowercase
    tokens = nltk.word_tokenize(text)             # tokenize
    tokens = [t for t in tokens if t not in string.punctuation]  # remove punctuation
    tokens = [t for t in tokens if t not in stop_words]          # remove stopwords
    tokens = [lemmatizer.lemmatize(t) for t in tokens]           # lemmatize
    return tokens
