from flask import Flask, jsonify, render_template
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return '<h1>Welcome to the URL Shortener</h1>'

if __name__ == '__main__':
    app.run(debug=True)

