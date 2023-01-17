import sqlite3

DB = './DB/TEST.db'

conn = sqlite3.connect(DB)

cur = conn.cursor()

print("Database created/connected!")

# Check current DB entries

cur.execute('SELECT * FROM persons')
for row in cur:
	print(row)

# Query for deleting from DB
sql_query = """DELETE FROM persons WHERE name IN ({0})"""

names = ["John", "Hanna"]
#  Query below is from answer on: https://stackoverflow.com/questions/14142554/sqlite3-python-executemany-select
## This query passes a list of values for the Query to check
cur.execute(sql_query.format(', '.join('?' for _ in names)), names)

print("\nAfter DELETE")

cur.execute('SELECT * FROM persons')
for row in cur:
	print(row)

# Don't commit so we can observe the results of the query

cur.close()
conn.close()