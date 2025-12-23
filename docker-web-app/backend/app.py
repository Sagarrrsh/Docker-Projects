from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="appdb",
        user="admin",
        password="admin"
    )

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/users")
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

app.run(host="0.0.0.0", port=5000)
