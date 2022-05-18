from crypt import methods
import re
from urllib import request
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from werkzeug import exceptions
from controllers import urls

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/all', methods = ['GET'])
def all():
    all_urls = urls.get_all()
    return jsonify(all_urls)

if __name__ == '__main__':
    app.run(debug=True)

