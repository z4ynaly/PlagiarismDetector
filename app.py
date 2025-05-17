from flask import Flask, render_template, request
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and vectorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf_vectorizer = pickle.load(vectorizer_file)

# Function to detect plagiarism
def detect(text):
    vectorized_text = tfidf_vectorizer.transform([text])
    prediction = model.predict(vectorized_text)
    return "Plagiarism Detected" if prediction[0] == 1 else "No Plagiarism Detected"

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle plagiarism detection
@app.route('/detect', methods=['POST'])
def detect_plagiarism():
    input_text = request.form.get('text')
    result = detect(input_text)
    return render_template('index.html', result=result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
