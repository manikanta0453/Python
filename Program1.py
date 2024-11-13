import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="rkce",

)
c=mydb.cursor()
c.execute("create table employee (eid int, ename varchar(30), city varchar(30))")