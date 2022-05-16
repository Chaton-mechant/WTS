#!/usr/bin/env python

import sqlite3

class Wts:
    """
    WTS class
    This class is used to manage sqlite database
    The main purpose of this class is to execute sql commands
    """

    def __init__(self, sqlite_path: str):
        """
        Initialize the connection to the sqlite db and create the cursor
        """
        self.sqlite_path = sqlite_path
        self.conn = sqlite3.connect(self.sqlite_path)
        self.cursor = self.conn.cursor()

    def __del__(self):
        """
        Stop the connection to the sqlite db
        """
        self.conn.close()

    ################################################################################
    # The function that read and execute sql command from sql file in the sqlite db
    # @param sql_file_path: the path of the sql file
    # @return: None
    # @exception: None
    # @note: None
    # @example: None
    ################################################################################

    def execute_sql_file(self, sql_file_path: str):
        """
        Execute the sql command from the sql file in the sqlite db
        """
        with open(sql_file_path, 'r') as f:
            # read the file with utf-8 encoding
            sql_commands = f.read()
        self.cursor.executescript(sql_commands)
        self.conn.commit()
        self.__del__()


Wts("exemple.sqlite").execute_sql_file("exemple.sql")
