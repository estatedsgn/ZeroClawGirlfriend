import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
TELEGRAM_TOKEN = "8585024363:AAGMpuY6nkkZ3FzGS60WFBO0v313eMs8ak4"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "message" in data:
        message = data["message"]
        if isinstance(message, dict) and "text" in message:
            text = message["text"]
            # Send response back to Telegram
            chat_id = message.get("chat", {}).get("id", "")
            if chat_id:
                response_text = f"Привет, Яхве! Я твоя Подруга. Ты сказал: {text}"
                requests.post(
                    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                    json={chat_id: chat_id, text: response_text}
                )
    return jsonify({status: "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

