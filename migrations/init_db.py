import sqlite3

connection = sqlite3.connect('database.db')


with open('./migrations/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# insert some users
cur.execute("INSERT INTO users (username) VALUES (?)", ('admin',))

cur.execute("INSERT INTO users (username) VALUES (?)", ('demo',))

connection.commit()
connection.close()
