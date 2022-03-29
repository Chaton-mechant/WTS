#!/usr/bin/env python


import sqlite3

def wts(data_file:str, sqlite_file:str):
    """
    @pre: - Enter the sql file name wich contains all the sql 
            instructions : `data_file` and the sqlite file name : `sqlite_file`
    @post: - The sqlite file is created and filled with the data from the
    """
    # Access to the sqlite file
    conn = sqlite3.connect(sqlite_file) 

    # the cursor is used to execute the sql instructions
    cursor = conn.cursor()

    with open (data_file,'r') as dataf: 

        for lines in dataf:
            the_insert = lines.split(";")   
            cursor.execute('''{}'''.format(the_insert[0]))

    # If the data is inserted, commit the changes
    conn.commit()

    # close the connection to the database
    conn.close()


wts("exemple_cmd.sql","exemple_database.sqlite")