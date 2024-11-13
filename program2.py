import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="rkce",

)
c=mydb.cursor()
c.execute("insert into employee values(102, 'Pavan', 40000)")
mydb.commit()