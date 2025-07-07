# Classplus Token Extractor API

A lightweight Flask API to extract login token from Classplus app using phone, orgCode, and OTP.

## 🌐 Live Endpoints

- `POST /send-otp` - Initiates OTP
- `POST /verify-otp` - Verifies OTP and returns login token

## 🚀 Deploy to Render

Click the button to deploy:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

Set the environment variables:

- `API_ID`
- `API_HASH`
- `BOT_TOKEN`
