from flask import Flask, request, jsonify, session
from flask_cors import CORS
import sqlite3
from jarvis_engine import process_command

app = Flask(__name__)
app.secret_key = "jarvis_secret_key"

CORS(app, resources={r"/*": {"origins": "*"}})


# =========================
# HOME
# =========================
@app.route("/")
def home():
    return "Jarvis Backend Running 🚀"


# =========================
# INIT DB
# =========================
def init_db():
    conn = sqlite3.connect("messages.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()


# =========================
# CONTACT
# =========================
@app.route("/contact", methods=["POST"])
def contact():
    data = request.json

    conn = sqlite3.connect("messages.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
        (data.get("name"), data.get("email"), data.get("message"))
    )

    conn.commit()
    conn.close()

    return jsonify({"status": "success"})


# =========================
# LOGIN
# =========================
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    if data.get("username") == "admin" and data.get("password") == "1234":
        session["user"] = "admin"
        return jsonify({"status": "success"})

    return jsonify({"status": "failed"})


# =========================
# MESSAGES
# =========================
@app.route("/messages", methods=["GET"])
def get_messages():
    conn = sqlite3.connect("messages.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM messages")
    data = cur.fetchall()

    conn.close()

    return jsonify(data)


# =========================
# JARVIS AI BRAIN
# =========================
@app.route("/jarvis", methods=["POST"])
def jarvis():
    data = request.json
    command = data.get("command")

    response = process_command(command)

    return jsonify({
        "response": response,
        "status": "success"
    })


# =========================
# RUN SERVER (IMPORTANT)
# =========================
if __name__ == "__main__":
    app.run(debug=True)