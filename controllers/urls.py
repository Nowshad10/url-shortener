from flask import Flask
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_all():
    data = []
    conn = get_db_connection()
    all_urls = conn.execute('SELECT * FROM urls').fetchall()
    for u in all_urls:
        url_data = {
            "id": u["id"],
            "normal": u["normal"],
            "shortened": u["shortened"]
        }
        data.append(url_data)
    conn.close()
    return data

