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

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgres://helloworld_user:PrD3vf6KbhHx8E7jz8Kc2mLZZImgVyMz@dpg-co0s7oect0pc73fkttc0-a/helloworld_db_4f3d")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgres://helloworld_user:PrD3vf6KbhHx8E7jz8Kc2mLZZImgVyMz@dpg-co0s7oect0pc73fkttc0-a/helloworld_db_4f3d")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number) Values
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgres://helloworld_user:PrD3vf6KbhHx8E7jz8Kc2mLZZImgVyMz@dpg-co0s7oect0pc73fkttc0-a/helloworld_db_4f3d")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    html_string = "<h3>Data returned from DB query:</h3>"
    html_string += "<table>"
    for player in records:
        html_string += "<tr>"
        for info in player:
            html_string += "<td>{}</td>".format(info)
        html_string += "</tr>"
    html_string += "</table>"    
    return html_string

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgres://helloworld_user:PrD3vf6KbhHx8E7jz8Kc2mLZZImgVyMz@dpg-co0s7oect0pc73fkttc0-a/helloworld_db_4f3d")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"
