# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:31:28 2022

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
data = ("001","Johnson","25")

dbcursor.execute(sql,data)
con.commit()

print("success")