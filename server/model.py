import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re
import pickle
import warnings
warnings.filterwarnings("ignore")


class Model:
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Model, cls).__new__(cls)
            cls._instance.model = pickle.load(open("../Models/model.pkl", 'rb'))
            cls._instance.vectorizer = pickle.load(open("../Models/vectorizer.pkl", 'rb'))
            cls._instance.lemmatizer = WordNetLemmatizer()
            cls._instance.stop_words = set(stopwords.words('english'))
        return cls._instance

    def clean_and_lemmatize(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^\w\s!$@?]", "", text)  # Keep !, $, @, ?
        words = nltk.word_tokenize(text)
        words = [word for word in words if word not in self.stop_words]
        words = [self.lemmatizer.lemmatize(word) for word in words]
        return ' '.join(words)

    def extract_features(self, text: str) -> pd.DataFrame:
        total_number = len(re.findall(r'\d+', text))  
        text_length = len(text) 
        text_vectorized = pd.DataFrame(self.vectorizer.transform([text]).toarray(),
                                       columns=self.vectorizer.get_feature_names_out())
  
        features = pd.DataFrame([[total_number, text_length]], columns=['total_number', 'len'])
        
        return pd.concat([features, text_vectorized], axis=1)

    def predict(self, text: str) -> int:
        cleaned_text = self.clean_and_lemmatize(text)
        features = self.extract_features(cleaned_text)
        return self.model.predict(features)[0]
