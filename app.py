from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/api/users')
def get_users():
    name = request.args.get('name', '')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = ''{name}''")
    return {'users': cursor.fetchall()}

if __name__ == '__main__':
    app.run(debug=True)
