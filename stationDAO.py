# Adapted from A. Beatty (2019) Data Representation: Galway-Mayo Institute of Technology https://github.com/andrewbeattycourseware/dataRepresentation
from flask import Flask, jsonify, request, abort
import mysql.connector
import dbconfig as cfg
class StationDAO:
    db=""
    def connectToDB(self): 
        self.db = mysql.connector.connect(
        host=       cfg.mysql['host'],
        user=       cfg.mysql['user'],
        password=   cfg.mysql['password'],
        database=   cfg.mysql['database'],
        )
    
    def __init__(self):
        self.connectToDB()

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

            
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into station (name, fuel_type, zip) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        lastRowId=cursor.lastrowid
        cursor.close
        return lastRowId

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from station"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        cursor.close()
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from station where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        fuel_station=self.convertToDictionary(result)
        cursor.close()
        return fuel_station

    def update(self, values):
        cursor = self.db.cursor()
        sql="update station set name= %s,fuel_type=%s, zip=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from station where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        cursor.close()

    def convertToDictionary(self, result):
        colnames=['id','station_name','fuel_type_code', "zip"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
stationDAO = StationDAO()