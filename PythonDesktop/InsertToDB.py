import sqlite3

DB = './DB/TEST.db'

conn = sqlite3.connect(DB)

cur = conn.cursor()

print("Database created/connected!")

# Insert list of values into table "persons"

sql_query = """INSERT INTO persons VALUES(?, ?)"""

names = [
	(1, "John"), 
	(2, "Kelly"), 
	(3, "Hanna"), 
	(4, "Michael"),
	(5, "Jenny"),
	(6, "Connor")]

cur.execute('SELECT * FROM persons')

# Removes existing DB entries from list of people to add
for row in cur:
	#print(row)
	for person in names:
		if row == person:
			#print("In DB")
			del names[names.index(person)]


cur.executemany(sql_query, names)
print("Updated DB entries")

cur.execute('SELECT * FROM persons')
for row in cur:
	print(row)

conn.commit()

cur.close()
conn.close()