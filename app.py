from flask import Flask, jsonify, render_template, request
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

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        try:
            url = request.form['url']
            mini_url = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
            conn = get_db_connection()
            conn.execute("INSERT INTO urls (normal, shortened) VALUES (?,?) RETURNING *", (url, mini_url)).fetchall()
            conn.commit()
            conn.close()
        except:
            print('failed')
        finally:
            conn.close
            return render_template('index.html', shortened_url = f"localhost:5000/{mini_url}")


@app.route('/all', methods = ['GET'])
def all():
    all_urls = urls.get_all()
    return jsonify(all_urls)

if __name__ == '__main__':
    app.run(debug=True)

