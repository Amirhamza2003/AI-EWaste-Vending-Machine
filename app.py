from flask import Flask, request, jsonify
from google.cloud import aiplatform

app = Flask(__name__)

# Function to call Vertex AI Model
def predict_with_vertex(input_data):
    endpoint = "YOUR_VERTEX_AI_ENDPOINT"
    client = aiplatform.gapic.PredictionServiceClient()
    response = client.predict(endpoint=endpoint, instances=[input_data])
    return response.predictions

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json["input"]
    prediction = predict_with_vertex(data)
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True)
