import sqlite3

DB = './DB/TEST.db'

conn = sqlite3.connect(DB)

cur = conn.cursor()

print("Database created/connected!")

conn.close()