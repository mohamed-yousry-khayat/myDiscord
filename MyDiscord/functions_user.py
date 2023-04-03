import logging
import connect
import mysql.connector

mydb = connect.mydb
cursor = connect.cursor

def create_user(email, name, password, picture):
    try:
        command = "INSERT INTO users (`email`, `user name`, `password`, `picture`) VALUES (%s, %s, %s, %s)"
        values = (email, name, password, picture)
        cursor.execute(command, values)
        userID = cursor.lastrowid
        cursor.execute(f"INSERT INTO bio (`user id`) VALUES({userID})")
        mydb.commit()
        logging.info(f"Succesfully created user with email: {email}, user name: {name}, password: {password}")
        logging.info(f"new user created with email {email} and name {name}")
        return True
    except mysql.connector.errors.IntegrityError:
        logging.warning('User already exists')
        return False
    except:
        logging.error("Error creating new user")

def login(email, password):
    try:
        cursor.execute(f"SELECT * FROM mydb.users WHERE email='{email}' AND password='{password}';")
        id = cursor.fetchall()[0][0]
        with open('credentials.txt', 'w') as f:
            credentials = str(id) + '\n' + email + '\n' + password
            f.write(credentials)
        logging.info(f"Succesfully logged in with email {email}")
        import functions_chat
        functions_chat.get_user(email)
        return 0
    except IndexError:
        return 1
    except:
        return 2

def check_version():
    cursor.execute("SELECT * FROM Version")
    version = cursor.fetchall()
    if version[0][0] == connect.version:
        return True
    else: return False