import sqlite3


class DbConnection:
    conn: sqlite3.Connection

    @classmethod
    def __init__(cls):
        cls.conn = sqlite3.connect('database.db')
        cls.conn.row_factory = sqlite3.Row

    @classmethod
    def __open__(cls):
        return cls.conn

    @classmethod
    def __close__(cls, exc_type, exc_value, traceback):
        cls.conn.close()

    @classmethod
    def execute(cls, query, params=()):
        cursor = cls.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
