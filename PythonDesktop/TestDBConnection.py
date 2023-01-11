import sqlite3
conn = sqlite3.connect('./DB/TEST.db')

c = conn.cursor()

print("Database created/connected!")

conn.close()