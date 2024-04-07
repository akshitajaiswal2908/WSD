from flask import Flask, render_template, request, jsonify
import joblib
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)
loaded_model = joblib.load('logistic_regression_model.pkl')
loaded_vectorizer = joblib.load('tfidf_vectorizer.pkl')

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word.lower() for word in tokens]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    processed_text = ' '.join(tokens)
    return processed_text

def generate_response(user_input):
    preprocessed_input = preprocess_text(user_input)
    user_input_vectorized = loaded_vectorizer.transform([preprocessed_input])
    predicted_label = loaded_model.predict(user_input_vectorized)[0]
    return predicted_label

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form['user_input']
    computer_response = generate_response(user_input)
    return jsonify({"user_message": user_input, "computer_response": computer_response})

if __name__ == '__main__':
    app.run(debug=True)
