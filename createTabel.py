# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:19:02 2022

@author: mekii
"""

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "databaseName"
    
    )

if con.is_connected():
    print("success")

tabel = con.cursor()
tabel.execute("create table if not exists tabelName(id varchar(10),name varchar(10),age varchar(10))")
