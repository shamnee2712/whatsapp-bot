from flask import Flask, request, jsonify

app = Flask(__name__)

# Your custom verification token (set the same in Meta Dashboard)
VERIFY_TOKEN = "your_custom_token"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Meta verification
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403
    
    elif request.method == "POST":
        # Handle incoming messages
        data = request.json
        print("Received message:", data)
        return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
