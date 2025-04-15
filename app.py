from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received alert: {data}")
    # TODO: Add logic to process the alert and send orders to MT5
    return '', 200

if __name__ == '__main__':
   import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
