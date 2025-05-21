import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    )

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE TESDATABASE")