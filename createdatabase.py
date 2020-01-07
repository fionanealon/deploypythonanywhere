# Adapted from A. Beatty (2019) Data Representation: Galway-Mayo Institute of Technology https://github.com/andrewbeattycourseware/dataRepresentation
import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect(
    host=       cfg.mysql['host'],
    user=       cfg.mysql['user'],
    password=   cfg.mysql['password']
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE fionanealon4$datarep")