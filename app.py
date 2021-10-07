from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Motivitylabs! This is ramm from DevOps team !"
