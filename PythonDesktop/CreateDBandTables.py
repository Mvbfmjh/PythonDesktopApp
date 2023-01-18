## Execute this script to initialize the database FE3H.db

import sqlite3
import os


DB_PATH = './DB/'
DB_LIST = ['FE3H.db']

QUERYPATH = "./DB"
QueryFiles = []
CREATE_TABLE_QUERY = []

# Find all .sql query files
for filepath in os.listdir(QUERYPATH):
	file = filepath.split('.')
	if file[1] == "sql":
		#print(filepath + " is a .sql file")
		QueryFiles.append(filepath)

# Store query as a string
for sqlfile in QueryFiles:
	currpath = QUERYPATH + "\\" + sqlfile
	#print(currpath)
	if os.path.isfile(currpath):
		file = open(currpath, "r", encoding="utf-8")
		data = str(file.read())
		file.close()
		CREATE_TABLE_QUERY.append(data)

# Create DB and execute queries
for db_file in DB_LIST:

	trgt_db = DB_PATH + db_file
	conn = sqlite3.connect(trgt_db)

	cur = conn.cursor()

	print("Database created/connected!")

	for query in CREATE_TABLE_QUERY:
		cur.execute(query)

	print("Queries executed...")

	# Checking tables

	sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
	cur.execute(sql_query)
	for row in cur:
		print(row)

	cur.close()
	conn.close()

