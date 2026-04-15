import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    nome = os.getenv("NOME", "DevOps")
    return f"Olá {nome}"

app.run(host="0.0.0.0", port=5000)