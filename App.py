from flask import Flask, render_template, request, jsonify, session
from model import get_response

app = Flask(__name__)

app.secret_key = "chatbot-secret-key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    message = data["message"]
    personality = data["personality"]

    if "history" not in session:
        session["history"] = []

    history = session["history"]

    response = get_response(
        message,
        history,
        personality
    )

    history.append({
        "user": message,
        "bot": response
    })

    session["history"] = history

    return jsonify({
        "response": response
    })


@app.route("/clear", methods=["POST"])
def clear_chat():

    session.pop("history", None)

    return jsonify({
        "message": "Chat cleared"
    })


if __name__ == "__main__":
    app.run(debug=True)
    