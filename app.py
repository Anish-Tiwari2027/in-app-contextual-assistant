from flask import Flask, request, jsonify
from actions.action_engine import execute_action   # 👈 USE REAL LOGIC

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)
        text = data.get("text", "")

        result = execute_action(text)

        # 🔍 DEBUG
        print("DEBUG INPUT :", text)
        print("DEBUG INTENT:", result["intent"])
        print("DEBUG REPLY :", result["reply"])

        return jsonify(result)

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "intent": "error",
            "reply": "Something went wrong"
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
