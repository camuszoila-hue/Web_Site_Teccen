from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Configuración de la base de datos
def init_db():
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            video_id TEXT,
            texto TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT video_id, texto FROM comentarios')
    todos = cursor.fetchall()
    conn.close()
    return render_template('index.html', comentarios=todos)

@app.route('/agregar', methods=['POST'])
def agregar():
    video_id = request.form['video_id']
    texto = request.form['texto']
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO comentarios (video_id, texto) VALUES (?, ?)', (video_id, texto))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)