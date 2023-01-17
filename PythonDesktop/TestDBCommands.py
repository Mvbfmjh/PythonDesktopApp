import sqlite3

DB = './DB/TEST.db'

conn = sqlite3.connect(DB)

cur = conn.cursor()

print("Database created/connected!")

# Check all existing tables
## Query for SQLite3 to get all table names
sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""

cur.execute(sql_query)

rowCount = 0

for row in cur:
	print(row)
	rowCount += 1

print(rowCount)

if rowCount == 0:
	cur.execute(
		'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')

cur.execute(
	'SELECT * FROM sqlite_sequence')

for row in cur:
	print(row)

conn.close()