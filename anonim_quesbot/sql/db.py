import sqlite3


def add_to_db(user_id, user_name, username):
    with sqlite3.connect('database.sqlite') as db:
        cur = db.cursor()

        cur.execute('INSERT OR IGNORE INTO users (user_id, user_name, username) VALUES(?, ?, ?)', (user_id, user_name, username))


def get_user(user_id):
    with sqlite3.connect('database.sqlite') as db:
        cur = db.cursor()

        user = cur.execute('SELECT * FROM users WHERE user_id=?', (user_id,)).fetchone()

        if user:
            return True
        else:
            return False