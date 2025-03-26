'''
To reset the database, run this command in the Shell: 
  sqlite3 myDatabase.db ".read create.sql"
'''

import sqlite3

from flask import Flask, render_template, request

app = Flask('app')
app.debug=True

@app.route('/')
def index():
	connection = sqlite3.connect("myDatabase.db")
	cursor = connection.cursor()
	res=cursor.execute("SELECT * FROM courses")
	courses=res.fetchall()
	
	return render_template('index.html',courses=courses)
@app.route('/addstudent',methods=['GET','POST'])
def newStudent():

	if request.method== 'POST':
		conn = sqlite3.connect("myDatabase.db")
		print("getting post request")
		name=request.form["student_name"]
		gwid=request.form["student_id"]
		email=request.form["student_email"]
		sql = " INSERT INTO students VALUES(?,?,?)"
		# Create  a cursor
		conn = sqlite3.connect("myDatabase.db")
		cur = conn.cursor()
		# execute the INSERT statement
		inp=(gwid,name,email)
		cur.execute(sql,inp)
		# commit the changes
		conn.commit()
		conn.close()
	return render_template('addStudent.html')
		
app.run(host='0.0.0.0', port=8080)
