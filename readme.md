# Text Classification Flask App

This project is a Flask-based web application for classifying text into "Positive" or "Negative" categories using a machine learning model. It leverages natural language processing (NLP) techniques for preprocessing and a trained classification model for predictions.

---

## Project Setup

1. **Clone the Repository**:
   ```bash
   git clone (https://github.com/surajraghuwanshi05/imdb_review.git)
   cd (https://github.com/surajraghuwanshi05/imdb_review.git)
   ```

2. **Activate virtual envirnoment**
   ``` .venv\Scripts\Activate```
   
### OR 

** Create env**
``` python -m venv envname```

. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


## 📂 Data Acquisition

The dataset for training the model was sourced from `KAGGLE`.

### 🔄 Preprocessing Steps
1. Removing URLs and non-alphanumeric characters.
2. Converting text to lowercase.
3. Tokenizing the text.
4. Lemmatizing the tokens.
5. Removing stopwords.

### 🛠 Feature Extraction
The `TfidfVectorizer` from `scikit-learn` was used to convert the preprocessed text data into numerical features suitable for the machine learning model.


## 🚀 Run Instructions

### 1. Train the Model
If you need to train or retrain the model, run the training script in model_trainer cell by cell:



### 2. Start the Flask Server
To start the Flask server, run the following command:
```python main.py```

### 3. Test the Endpoint
Using the Web Interface:
1. Open http://127.0.0.1:5000/ in your web browser.
2. Enter a text sample in the input box.
3. Click the Classify button to see the prediction result.


## 📊 Model Info

### Model Approach
- The classification model is trained using **scikit-learn**.
- The algorithm used (e.g., Logistic Regression, Naive Bayes) is stored in the `model.pkl` file.
- Text is preprocessed using a **TF-IDF vectorizer** for numerical representation which is stored in `vectorizer.pkl` .

### Key Results
- The model achieved **89.31% accuracy**,  **89.37% F1 score** **88.10% precision** and **90.67% Recall**  on the validate  dataset.
- These results demonstrate its ability to classify text as positive or negative effectively.


## 📂 Project Structure

### 1. **Modules Overview**
- **`main.py`**  
  Contains the code for the **Flask app**, including routes for serving the web interface and handling classification requests.

- **`src/`**  
  This folder contains:
  - Jupyter notebooks and scripts for **model training** and experimentation.
  - Code for preprocessing, feature extraction, and model evaluation.

- **`database/`**  
  Includes the code for handling **SQLite database operations**, such as data insertion (`insert_data` module).

- **`artifacts/`**  
  Stores all the essential files generated during the project:
  - `model.pkl`: The trained machine learning model.
  - `vectorizer.pkl`: The fitted TF-IDF vectorizer.
  - `.csv` files: Dataset files used for training or testing.
  - `.db` files: SQLite database file used in the project.

- **`templates/`**  
  Contains the **HTML files** (`.html`) used to define the structure of the web interface for the Flask app.

- **`static/`**  
  Includes the **CSS files** and other static assets (like images or JavaScript files) used to style and enhance the web interface.

---

This structure ensures modularity and a clear separation of responsibilities, making it easy to maintain and extend the project.
