# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:40:12 2022

@author: mekii
"""

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    
    )


if con.is_connected():
    print("Success")
    
db = con.cursor()
db.execute("create database databaseName")
    