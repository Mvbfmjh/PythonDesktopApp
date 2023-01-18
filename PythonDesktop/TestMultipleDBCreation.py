import sqlite3

DB = './DB/TEST.db'
DB_PATH = './DB/'
DB_LIST = ['TEST.db', 'Trees.db', 'Home.db']

for db_file in DB_LIST:

	trgt_db = DB_PATH + db_file
	conn = sqlite3.connect(trgt_db)

	cur = conn.cursor()

	print("Database created/connected!")

	# Check all existing tables
	## Query for SQLite3 to get all table names
	sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""

	cur.execute(sql_query)

	for row in cur:
		print(row)

	conn.close()

