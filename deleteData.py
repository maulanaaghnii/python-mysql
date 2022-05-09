# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:02:50 2022

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

sql = "delete from tabelName where id = '006'"
dbcursor.execute(sql)

con.commit()
print("Delete Success")