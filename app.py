from flask import Flask
import sqlite3
import random
import json


connection = sqlite3.connect('database.db')
app = Flask(__name__)

facts_list = []
with open('facts.txt') as my_file:
    for line in my_file:
        facts_list.append(line.rstrip())


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for index, fact in enumerate(facts_list):
    cur.execute("INSERT INTO facts (title, fact) VALUES (?, ?)",
            (f'Random Fact {index}', fact)
            )

connection.commit()
connection.close()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def hello_world():
    return f"Generate a random fact using /fact route"
    

@app.route("/fact")
def generate_a_fact():
    random_key = random.randint(0, len(facts_list)-1)
    conn = get_db_connection()
    random_fact = conn.execute("SELECT * FROM facts").fetchall()
    conn.close()
    data_to_send = {random_fact[random_key][2]:random_fact[random_key][3]}
    print(data_to_send)
    json_data_to_send = json.dumps(data_to_send)
    return f"{json_data_to_send}"

if __name__ == "__main__":
    app.run()