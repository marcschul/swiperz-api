import psycopg2
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='swiperz_db',
                            user='swiperz',
                            password='swiperz')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM games;')
    games = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', games=games)

@app.route('/json')
def json():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM games;')
    games = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(games)

if __name__ == "__main__":
  app.run(debug=True)