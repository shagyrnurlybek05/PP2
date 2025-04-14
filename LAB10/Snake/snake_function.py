import psycopg2
import json

conn = psycopg2.connect(
    database="lab10",
    user="postgres",
    password="admin",
    host="localhost",
    port=5432
)
cur = conn.cursor()

def get_or_create_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        return user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        conn.commit()
        return cur.fetchone()[0]

def save_game(user_id, score, level, snake, direction, food):
    cur.execute("""
        INSERT INTO user_score (user_id, score, level, snake, direction, food)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (user_id, score, level, json.dumps(snake), direction, json.dumps(food)))
    conn.commit()

def load_last_state(user_id):
    cur.execute("SELECT * FROM user_score WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1", (user_id,))
    return cur.fetchone()
