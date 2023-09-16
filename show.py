import sqlite3
connection=sqlite3.connect('abc.db',check_same_thread=False)
cursor=connection.cursor()

cursor=connection.execute("select * from users");

for row in cursor:
    print("Id = ",row[0] )
    print("Fullname ",row[1])
    print("Email = ",row[2])
    print("Username = ",row[3] )
    print("Password = ",row[4] )
    print("Phone = ",row[5] )
    print("Address = ",row[6] )
    print("Skill = ",row[7] )
    
connection.commit()
cursor.close()
connection.close()