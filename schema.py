import sqlite3
connection=sqlite3.connect('abc.db',check_same_thread=False)
cursor=connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname varchar(40),
        email VARCHAR(15),
        username VARCHAR(20),
        password VARCHAR(15),
        mobile varchar(20),
        adderss varchar(20),
        skill varchar(30)
    );"""
)
