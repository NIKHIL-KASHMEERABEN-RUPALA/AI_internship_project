import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')

# Preprocess user input
def preprocess_text(text):
    # Tokenization
    words = word_tokenize(text.lower())
    
    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    
    return filtered_words

if __name__ == "__main__":
    text = input("Enter text for preprocessing: ")
    print(preprocess_text(text))
