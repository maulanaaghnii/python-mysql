# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:50:57 2022

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
sql = "select * from tabelName"
dbcursor.execute(sql)
data = dbcursor.fetchall()


for data in data:
    print(data)