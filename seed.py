import sqlite3
connection=sqlite3.connect('abc.db',check_same_thread=False)
cursor=connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password,
        f_c)VALUES(
            'Umar',
            'Mohammad',
            'Blue'
        
    );"""
)
connection.commit()
cursor.close()
connection.close()