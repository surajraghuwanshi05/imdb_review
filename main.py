from flask import Flask, render_template, request
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import nltk
import pickle

app = Flask(__name__)

# Load the trained model
with open("artifacts/model.pkl", "rb") as c:
    model = pickle.load(c)

# Load the fitted TF-IDF vectorizer
with open("artifacts/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Placeholder function for text classification
def classify_text(text):
    lemma = WordNetLemmatizer()
    swords = stopwords.words("english")
    text = re.sub(r'https\S+', '', text)

    # cleaning everything except alphabetical and numerical characters
    text = re.sub("[^a-zA-Z0-9]", " ", text)

    # Tokenizing and lemmatizing
    text = nltk.word_tokenize(text.lower())
    text = [lemma.lemmatize(word) for word in text]

    # Removing stopwords
    text = [word for word in text if word not in swords]

    # Joining
    text = " ".join(text)

    # Vectorize the input text
    text_vectorized = vectorizer.transform([text])

    # Predict using the model
    prediction = model.predict(text_vectorized)
    if prediction[0] == 0:
        return "Negative"
    elif prediction[0] == 1:
        return "Positive"


@app.route("/")
def home():
    return render_template("index.html", result=None)

@app.route("/classify", methods=["POST"])
def classify():
    text = request.form["inputText"]
    result = classify_text(text)
    return render_template("index.html", result=result)

@app.route("/clear", methods=["GET", "POST"])
def clear():
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
