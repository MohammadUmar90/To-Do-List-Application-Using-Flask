import sqlite3


def show_color(username):
    connection = sqlite3.connect('abc.db',check_same_thread= False)
    cursor = connection.cursor()
    cursor.execute("""SELECT f_c  FROM USERS WHERE username='{username}' ORDER BY pk DESC;""".format(username=username))
    color= cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    message = '{username}\'s favorite color is {color}.'.format(username=username,color=color)
    return message 

def cp(username):
    connection=sqlite3.connect('abc.db',check_same_thread=False)
    cursor=connection.cursor()
    cursor.execute("""SELECT password  FROM USERS WHERE username='{username}' ORDER BY pk DESC;""".format(username=username))
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    return password

def cs():
    connection=sqlite3.connect('abc.db',check_same_thread=False)
    cursor=connection.cursor()
    cursor.execute("""SELECT username FROM USERS  ORDER BY pk DESC;""")
    db_users = cursor.fetchall()
    users = []
    for i in range(len(db_users)):
        person=db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()
    return users

def profile(username):
    connection = sqlite3.connect('abc.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT pk, fullname, email,username,password,mobile,adderss,skill FROM users WHERE username = '{username}' ORDER BY pk DESC; """.format(username= username))
    user = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return user

def signup(fullname,email,username,password,mobile,adderss,skill):
    connection=sqlite3.connect('abc.db',check_same_thread=False)
    cursor=connection.cursor()
    cursor.execute("""SELECT password FROM users WHERE username='{username}';""".format(username=username))
    e=cursor.fetchone()
    if e is None:
        cursor.execute("""INSERT INTO users(
        fullname,
        email,
        username,
        password,
        mobile,
        adderss,
        skill)
        VALUES(
            '{fullname}',
            '{email}',
            '{username}',
            '{password}',
            '{mobile}',
            '{adderss}',
            '{skill}'
            
        ); """.format(fullname = fullname ,  email = email, username=username, password=password ,mobile=mobile,adderss=adderss,skill=skill))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        return ('User  Alredy existed!!!!')


    return 'You have successfully signed up'