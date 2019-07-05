import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pos_perpus"
)
q = mydb.cursor()

def show(tabel, vals=[]):
	
	# select = ['judul','image']

	val = str(vals)
	replace = (("'","`"),("[",""),("]","")) 
	for x in replace:
		val = val.replace(*x)	

	
	q.execute("SELECT "+val+" FROM `"+tabel+"`")
	data = q.fetchall()

	return data

def all(tabel):

	q.execute("SELECT * from `"+tabel+"`")
	data = q.fetchall()

	return data

def add(tabel, vals=[]):

	val = str(vals)
	replace = (("[",""),("]",""),("None","NULL"))
	for x in replace:
		val = val.replace(*x)


	q.execute("INSERT INTO `"+tabel+"` VALUES ("+val+");")
	mydb.commit()
	return

def delete(tabel,id):

	q.execute("DELETE FROM `"+tabel+"` WHERE `"+tabel+"`.`id` = "+id+"")
	mydb.commit()
	return
