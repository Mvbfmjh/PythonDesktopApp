import os

#QUERYPATH = os.getcwd() + "\\DB"
QUERYPATH = "./DB"
QueryFiles = []
CREATE_TABLE_QUERY = []

for filepath in os.listdir(QUERYPATH):
	file = filepath.split('.')
	if file[1] == "sql":
		#print(filepath + " is a .sql file")
		QueryFiles.append(filepath)

for sqlfile in QueryFiles:
	currpath = QUERYPATH + "\\" + sqlfile
	#print(currpath)
	if os.path.isfile(currpath):
		file = open(currpath, "r", encoding="utf-8")
		data = str(file.read())
		file.close()
		CREATE_TABLE_QUERY.append(data)

for query in CREATE_TABLE_QUERY:
	print(query)