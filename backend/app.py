from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("fraud_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = [[
        data["age"],
        data["claim_amount"],
        data["previous_claims"]
    ]]

    prediction = model.predict(features)[0]

    if prediction == 1:
        status = "Rejected"
        fraud = "Fraud Detected"
    else:
        status = "Approved"
        fraud = "No Fraud"

    return jsonify({
        "status": status,
        "fraud": fraud
    })

@app.route("/users", methods=["GET"])
def home():
    return "Backend Running"

if __name__ == "__main__":
    app.run(debug=True)