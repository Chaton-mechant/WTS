#!/usr/bin/env python

import sqlite3

def write_to_schema(data_file:str, sqlite_file:str):
    """
    pre: - Introduire le nom du fichier sql que l'on veut 
            mettre dans le schema : `data_file` et le fichier
            sqlite dans lequel doit etre creer le 
            tableau : `sqlite_file`
    post: - Les données sont écrite sur `sqlite_file`
    """
    # Accès à la base de données
    conn = sqlite3.connect(sqlite_file) #'Chinook_Sqlite.sqlite'

    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()

    with open (data_file,'r') as dataf: #'insert_animaux_types.sql'

        for lines in dataf:
            the_insert = lines.split(";")   
            cursor.execute('''{}'''.format(the_insert[0]))

    # Si on a fait des modifications à la base de données
    conn.commit()

    # Toujours fermer la connexion quand elle n'est plus utile
    conn.close()


#list_sql = ["insert_animaux_types.sql", "insert_animaux_velages.sql", "insert_animaux.sql",
#"insert_complications.sql", "insert_familles.sql", "insert_types.sql", "insert_velages_complications.sql",
#"insert_velages.sql"]
#for files in list_sql:
#    write_to_schema(files, 'test.sqlite')
