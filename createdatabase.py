import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Data2019"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE datarep")