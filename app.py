import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("API Key is missing! Add it to the .env file.")

# Configure Gemini API
genai.configure(api_key=API_KEY)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json["input"]
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(data)
    return jsonify({"prediction": response.text})

if __name__ == '__main__':
    app.run(debug=True)
