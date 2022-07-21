import sqlite3 as db

connections=db.connect('STUDENT.db')

create_table=(''' CREATE TABLE IF NOT EXISTS STUD
                  (ID INTEGER PRIMARY KEY,
                  NAME  TEXT NOT NULL,
                  GRADE INTEGER NOT NULL);''');

connections.execute(create_table)
connections.close()                  
