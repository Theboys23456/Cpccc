import os
from flask import Flask, request, jsonify
import requests

API_ID = os.environ.get("API_ID", "your_default_api_id")
API_HASH = os.environ.get("API_HASH", "your_default_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_default_bot_token")

app = Flask(__name__)

@app.route("/send-otp", methods=["POST"])
def send_otp():
    data = request.json
    phone = data.get("phone")
    org_code = data.get("orgCode")

    if not phone or not org_code:
        return jsonify({"error": "Missing phone or orgCode"}), 400

    try:
        response = requests.post(
            "https://www.classplusapp.com/api/v2/user/loginWithPhone",
            json={
                "phone": phone,
                "countryCode": "+91",
                "orgCode": org_code
            }
        )
        return jsonify({"message": "OTP sent if details are valid."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    data = request.json
    phone = data.get("phone")
    org_code = data.get("orgCode")
    otp = data.get("otp")
    device_id = data.get("deviceId", "random-device")

    if not all([phone, org_code, otp]):
        return jsonify({"error": "Missing fields"}), 400

    try:
        res = requests.post(
            "https://www.classplusapp.com/api/v2/user/verifyOtp",
            json={
                "otp": otp,
                "phone": phone,
                "countryCode": "+91",
                "orgCode": org_code,
                "deviceId": device_id
            }
        )
        res.raise_for_status()
        return jsonify({
            "token": res.json().get("token"),
            "api_id": API_ID,
            "api_hash": API_HASH,
            "bot_token": BOT_TOKEN
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "✅ Classplus Token Extractor API is live!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
