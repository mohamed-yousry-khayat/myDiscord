import logging
import connect

mydb = connect.mydb
cursor = connect.cursor

with open('credentials.txt', 'r') as f:
    CurrentUserID, email, password = f.read().split()

def get_dm_messages(dmID):
    cursor.execute(f"SELECT `dm messages`.*, users.`user name` FROM `dm messages`, users  WHERE `dm id` = {dmID} AND `sender user id` = users.`user id` ORDER BY `time sent`;")
    messages = []
    for x in cursor:
        messages.append(x)
    cursor.reset()
    return messages #Returns list in the format [(MessageID, MessageText, SenderUserID, DMID, SenderUsername), (MessageID, MessageText, SenderUserID, DMID, SenderUsername)]

def get_latest_dm_messages(dmID, lastMessageID):
    cursor.execute(f"SELECT `dm messages`.*, users.`user name` FROM `dm messages`, users WHERE `message id` > {lastMessageID} AND `dm id` = {dmID} AND `sender user id` = users.`user id` ORDER BY `time sent`;")
    messages = []
    for x in cursor:
        messages.append(x)
    return messages #Returns list in the format [(MessageID, MessageText, SenderUserID, DMID, SenderUsername), (MessageID, MessageText, SenderUserID, DMID, SenderUsername)]

def get_dm_users():
    cursor.execute(f"SELECT * FROM `dm members` WHERE `user id` = {CurrentUserID}")
    ids = []
    dms = cursor.fetchall()
    for x in dms:
        cursor.execute(f"SELECT `dm members`.*, users.`user name`, users.picture FROM `dm members`, users WHERE `dm members`.`dm id` = {x[1]} and `dm members`.`user id` != {CurrentUserID} AND `dm members`.`user id` = `users`.`user id`;")
        dm_ids = cursor.fetchall()
        ids.append(dm_ids[0])
    return ids #Returns list in the format [(UserID, DMID, UserName), (UserID, DMID, UserName)]
 
def send_dm_messages(dmID, message):
    values = (message, CurrentUserID, dmID)
    command = "INSERT INTO `dm messages` (`message text`, `sender user id`, `dm id`) VALUES (%s, %s, %s);"
    cursor.execute(command, values)
    mydb.commit()

def get_user(email):
    cursor.execute(f" SELECT * FROM users WHERE email = '{email}'")
    info = cursor.fetchone()
    if info == None:
        return info
    user = []
    for index in range(len(info) - 1):
        user.append(info[index])
    with open('ProfilePictures/' + str(info[0]) + '.png', 'wb') as file:
        file.write(info[4])
    return user

def new_dm(userID):
    cursor.execute("INSERT INTO `dm id`(`dm id`) VALUES(NULL)")
    dmID = cursor.lastrowid
    mydb.commit()
    cursor.execute(f"INSERT INTO `dm members`(`user id`, `dm id`) VALUES({CurrentUserID}, {dmID})")
    cursor.execute(f"INSERT INTO `dm members`(`user id`, `dm id`) VALUES({userID}, {dmID})")
    mydb.commit()

def get_bio(userID):
    cursor.execute(f"SELECT * FROM bio WHERE `user id` = {userID}")
    bio = cursor.fetchone()
    return bio

def profile_update(email, username, password):
    values = (email, username, password, CurrentUserID)
    command = "UPDATE `users` SET `email` = %s, `user name` = %s, `password` = %s WHERE `user id` = %s"
    cursor.execute(command, values)
    mydb.commit()
    cursor.execute(f"SELECT * FROM `users` WHERE `user id` = {CurrentUserID}")
    credentials = cursor.fetchone()
    with open('credentials.txt', 'w') as f:
            credentialsString = str(credentials[0]) + '\n' + credentials[1] + '\n' + credentials[3]
            f.write(credentialsString)
    read_credentials()

def update_bio(about):
    command = "UPDATE bio SET `About Me` = %s WHERE `user id` = %s"
    values = (about, CurrentUserID)
    cursor.execute(command, values)
    mydb.commit()

def read_credentials():
    global CurrentUserID, email, password
    with open('credentials.txt', 'r') as f:
        CurrentUserID, email, password = f.read().split()

def unfriend(dmID):
    cursor.execute(f"DELETE FROM `dm messages` WHERE `dm id` = {dmID}")
    cursor.execute(f"DELETE FROM `dm members` WHERE `dm id` = {dmID}")
    cursor.execute(f"DELETE FROM `dm id` WHERE (`dm id` = {dmID})")

def update_pfp(picture):
    command = "UPDATE `users` SET picture = %s WHERE `user id` = %s"
    values = (picture, CurrentUserID)
    cursor.execute(command, values)
    mydb.commit()

def update_socials(facebook,instagram,spotify,youtube):
    command = f'UPDATE bio SET Instagram = %s, Spotify = %s, Facebook = %s, Youtube = %s WHERE `user id` = {CurrentUserID}'
    record = (instagram,spotify,facebook,youtube)
    cursor.execute(command,record)
    mydb.commit()

def submit_rating(slider, message):
    feedbackRecord = (CurrentUserID , slider, message)
    command = f'INSERT INTO feedback(`user id`, `rating`, `feedback`) VALUES(%s,%s,%s)'
    cursor.execute(command, feedbackRecord)
    mydb.commit()
