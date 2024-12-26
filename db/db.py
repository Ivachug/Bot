# db/db.py
import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT,
                        chat_id INTEGER)''')
    conn.commit()
    conn.close()

def add_user(user_id, username, chat_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (user_id, username, chat_id) VALUES (?, ?, ?)', 
                       (user_id, username, chat_id))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Пользователь уже есть в базе
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

