#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('coolbooks.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE Book
         (ID VARCHAR (256) PRIMARY KEY     NOT NULL,
         TITLE           TEXT    NOT NULL,
         AUTHOR            TEXT NOT NULL,
         DESCRIPTION TEXT);''')

print ("Table created successfully")

conn.close()