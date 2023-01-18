##  WIP

import sqlite3


DB_PATH = './DB/'
DB_LIST = ['FE3H.db']

for db_file in DB_LIST:

	trgt_db = DB_PATH + db_file
	conn = sqlite3.connect(trgt_db)

	cur = conn.cursor()

	print("Database created/connected!")


