## Execute this script to initialize the database FE3H.db

import sqlite3
import os


DB_PATH = './DB/'
DB_LIST = ['FE3H.db']

QUERYPATH = "./DB"
QueryFiles = []
QUERY = []

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
		query = data.split(';')
		for q in query:
			QUERY.append(q)

# Create DB and execute queries
for db_file in DB_LIST:

	trgt_db = DB_PATH + db_file
	conn = sqlite3.connect(trgt_db)

	cur = conn.cursor()

	print("Database created/connected!")

	for query in QUERY:
		print(query + '\n')
		try: 
			cur.execute(query)
		except NameError:
			print("Name Error")
		except ValueError:
			print("Value error")
		except IOError:
			print("IO error")
		except sqlite3.IntegrityError:
			print("Data Integrity Error: Failed to execute query... (Maybe Data exists already?)")

	print("Queries executed...")

	# Checking tables

	sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
	cur.execute(sql_query)
	for row in cur:
		print(row)


	cur.close()
	conn.commit()
	conn.close()

