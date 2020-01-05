import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect(
    host=       cfg.mysql['host'],
    user=       cfg.mysql['user'],
    password=   cfg.mysql['password'],
    database=   cfg.mysql['database'],
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE fionanealon1$datarep")