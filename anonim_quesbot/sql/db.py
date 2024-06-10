import sqlite3

def add_to_db(user_id, user_name, username):
    '''
    Добавляем пользователя в БД если его нету, если есть, то игнорируем запрос
    '''
    with sqlite3.connect('database.sqlite') as db:
        cur = db.cursor()

        cur.execute('INSERT OR IGNORE INTO users (user_id, user_name, username) VALUES(?, ?, ?)', (user_id, user_name, username))


def get_user(user_id):
    with sqlite3.connect('database.sqlite') as db:
        '''
        Функция, которая делает проверку на то, есть ли пользователь в БД
        '''
        cur = db.cursor()

        user = cur.execute('SELECT * FROM users WHERE user_id=?', (user_id,)).fetchone()

        if user:
            return True
        else:
            return False
        
def update_user(user_id, user_name, username):
    '''
    Функция, которая обновляет данные пользователя из БД 
    '''
    with sqlite3.connect('database.sqlite') as db:
        cur = db.cursor()

        cur.execute('UPDATE users set user_name = ?, username = ? where user_id = ?', (user_name, username, user_id))

def get_stat():
    '''
    Запрос к БД, где мы получаем всех пользователей, для дальнейшего вывода статистики
    '''
    with sqlite3.connect('database.sqlite') as db:
        cur = db.cursor()

        stat = cur.execute('SELECT id FROM users').fetchall()

        return len(stat)
