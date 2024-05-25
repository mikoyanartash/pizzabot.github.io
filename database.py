import sqlite3

def initialize_db():
    conn = sqlite3.connect('pizza_game.db')
    c = conn.cursor()
    
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        coins INTEGER DEFAULT 10
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS achievements (
        user_id INTEGER,
        achievement TEXT,
        PRIMARY KEY (user_id, achievement)
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS power_ups (
        user_id INTEGER,
        power_up TEXT,
        duration INTEGER,
        PRIMARY KEY (user_id, power_up)
    )''')

    conn.commit()
    conn.close()

def get_user_data(user_id):
    conn = sqlite3.connect('pizza_game.db')
    c = conn.cursor()
    c.execute('SELECT coins FROM users WHERE user_id = ?', (user_id,))
    user = c.fetchone()
    conn.close()
    if user:
        return {'coins': user[0]}
    else:
        return {'coins': 10}

def update_user_data(user_id, coins):
    conn = sqlite3.connect('pizza_game.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO users (user_id, coins) VALUES (?, ?)', (user_id, coins))
    conn.commit()
    conn.close()

def get_power_up(user_id):
    conn = sqlite3.connect('pizza_game.db')
    c = conn.cursor()
    c.execute('SELECT power_up, duration FROM power_ups WHERE user_id = ?', (user_id,))
    power_up = c.fetchone()
    conn.close()
    return power_up

def award_achievement(user_id, achievement):
    conn = sqlite3.connect('pizza_game.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO achievements (user_id, achievement) VALUES (?, ?)', (user_id, achievement))
    conn.commit()
    conn.close()
