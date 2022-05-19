from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS
from werkzeug import exceptions
from controllers import urls
import sqlite3
import string
import random

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def shorten_url():
    conn = get_db_connection()
    while True:
        rand_letters = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
        short_url = conn.execute("SELECT shortened FROM urls WHERE shortened = ?", (rand_letters,)).fetchone()
        if not short_url:
            return rand_letters

@app.route('/', methods = ['GET', 'POST'])
def home():
    conn = get_db_connection()
    if request.method == 'POST':
        url_to_shorten = request.form['url']
        found_url_obj = conn.execute("SELECT shortened FROM urls WHERE normal = ?", (url_to_shorten,)).fetchone()
        if found_url_obj:
            found_url = found_url_obj[0]
            return redirect(url_for("display_result", url=found_url))
        else:
            short_url = shorten_url()
            conn.execute("INSERT INTO urls (normal, shortened) VALUES (?,?)", (url_to_shorten, short_url))
            conn.commit()
            conn.close()
            return redirect(url_for("display_result", url=short_url))
    else:
        return render_template('home.html')

@app.route('/result/<url>')
def display_result(url):
    return render_template('result.html', short_url_display=url)

@app.route('/<shorty>')
def redirect_url(shorty):
    conn = get_db_connection()
    long_url = conn.execute("SELECT normal FROM urls WHERE shortened = ?", (shorty,)).fetchone()
    if long_url:
        return redirect(long_url["normal"])
    else:
        return f"<h1>Oops that url doesn't exist</h1>"

@app.route('/all', methods = ['GET'])
def all():
    all_urls = urls.get_all()
    return jsonify(all_urls)

if __name__ == '__main__':
    app.run(debug=True)

