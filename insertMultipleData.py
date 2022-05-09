# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:41:19 2022

@author: mekii
"""

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "databaseName"
    
    )

dbcursor = con.cursor()

sql = "insert into tabelname (id,name,age) values (%s,%s,%s)"
data = [("002","Alexander","30"),
        ("003","Mark","46"),
        ("004","James","19"),
        ("005","Stephen","26"),
        ("006","Cristian","50"),]
        
for val in data:
    dbcursor.execute(sql,val)
    con.commit()

print("success")