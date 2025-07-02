from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os
import time

app = Flask(__name__)
CORS(app)

def get_db_connection():
    # Esperar un poco para asegurarse que la base de datos esté lista
    time.sleep(2)
    return psycopg2.connect(
        host="db",
        database="inmobiliaria",
        user="admin",
        password="admin123"
    )

@app.route('/api/propiedades')
def get_propiedades():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM propiedades;')
    propiedades = [{'id': row[0], 'direccion': row[1]} for row in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(propiedades)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 