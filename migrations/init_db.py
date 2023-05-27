import sqlite3

connection = sqlite3.connect('database.db')

try:
    with open('./migrations/schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    # insert some users
    cur.execute("INSERT INTO users (username) VALUES (?)", ('admin',))

    cur.execute("INSERT INTO users (username) VALUES (?)", ('demo',))

    connection.commit()
    print("User table created successfully")
except Exception as e:
    print("User table creation failed", e)
finally:
    connection.close()
