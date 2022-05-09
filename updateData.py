# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:57:34 2022

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
sql = "update tabelName set name=%s, age=%s where id=%s"
data = "Durrant","38","001"

dbcursor.execute(sql,data)

con.commit()