import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="hospital")
mycury=mydb.cursor()
mycury.execute("delete from  hospital.pharma where AVAILABLE_FLAG='N';")