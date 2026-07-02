from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Yahan apna WhatsApp Token aur Phone Number ID paste karna hai baad me
WHATSAPP_TOKEN = "PASTE_YOUR_TOKEN_HERE" 
PHONE_NUMBER_ID = "PASTE_YOUR_PHONE_ID_HERE"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Meta Verification ke liye
        verify_token = "aali123" 
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode == "subscribe" and token == verify_token:
            return challenge, 200
        else:
            return "Verification failed", 403
    
    if request.method == "POST":
        data = request.get_json()
        print(data) # Abhi ke liye sirf log kar rahe hain
        return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
