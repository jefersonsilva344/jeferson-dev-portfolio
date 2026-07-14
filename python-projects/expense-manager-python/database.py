import sqlite3


connection = sqlite3.connect(
    "database.db"
)


cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY,
description TEXT,
amount REAL,
date TEXT
)
""")


connection.commit()

connection.close()
