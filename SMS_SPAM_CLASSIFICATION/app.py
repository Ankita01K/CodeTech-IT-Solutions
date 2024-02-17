import streamlit as st
import pickle 
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer

# Download NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

def transform_text(text):
    # Convert to lowercase and tokenize
    words = nltk.word_tokenize(text.lower())
    
    # Remove non-alphanumeric characters
    words = [i for i in words if i.isalnum()]
    
    # Remove stopwords and punctuation
    words = [i for i in words if i not in stopwords.words('english') and i not in string.punctuation]
    
    # Apply stemming
    words = [PorterStemmer().stem(i) for i in words]
    
    return " ".join(words)

tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))


st.title("Email/SMS Spam Classifier")

input_sms=st.text_area("Enter the Message")

if st.button("Predict"):
#1-preprocess
  transformed_sms=transform_text(input_sms)

#2-vectorize

  vector_input=tfidf.transform([transformed_sms])

#3-predict

  result=model.predict(vector_input)[0]

#4-Display
  if result == 1:
    st.header("Spam")
  else:
    st.header("Not Spam")
