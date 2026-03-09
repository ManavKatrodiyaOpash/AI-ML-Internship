import re
import string
from chatwords import chat_words

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')

def preprocess_text(text):

    # 1 Lowercase
    text = text.lower()

    # 2 Remove HTML tags
    text = re.sub(r"<.*?>","",text)

    # 3 Remove URLs
    text = re.sub(r"http\S+|www\S+","",text)

    # 4 Remove emojis
    text = re.sub(r"[^\w\s]", "", text)

    # 5 Tokenization
    tokens = word_tokenize(text)

    # 6 Chat word treatment
    new_tokens = []
    for word in tokens:
        if word in chat_words:
            new_tokens.extend(chat_words[word].split())
        else:
            new_tokens.append(word)

    tokens = new_tokens

    # 7 Remove punctuation
    tokens = [w.translate(str.maketrans('', '', string.punctuation)) for w in tokens]

    # 8 Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # 9 Spelling normalization (reduce repeated characters)
    tokens = [re.sub(r"(.)\1+", r"\1\1", word) for word in tokens]

    # 10 Stemming
    tokens = [stemmer.stem(word) for word in tokens]

    # 11 Lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Join tokens
    return " ".join(tokens)