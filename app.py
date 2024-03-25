import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Cameron Braatz in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://helloworld_user:PrD3vf6KbhHx8E7jz8Kc2mLZZImgVyMz@dpg-co0s7oect0pc73fkttc0-a/helloworld_db_4f3d")
    conn.close()
    return "Database Connection Successful"
