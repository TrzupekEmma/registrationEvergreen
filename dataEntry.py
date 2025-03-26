import sqlite3
filename='basicData.csv'
con = sqlite3.connect("myDatabase.db");
cur = con.cursor()
with open(filename,"r") as file:
	for line in file:
		print(line.strip())
		values=[]
		for value in line.strip().split('\t'):
			if value=="None":
				values.append(None);
			else:
				values.append(value)
		cur.execute("insert into courses values (?,?,?,?,?,?)",values)
	con.commit()
