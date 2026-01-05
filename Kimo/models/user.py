from utils import db 

def get_user_by_name(user_name):
    return db.fetch_one('SELECT * FROM userInfo WHERE user_name=%s', [user_name])

def get_user_by_email(email):
    return db.fetch_one('SELECT * FROM userInfo WHERE email=%s', [email])

def get_user_by_name_or_email(identifier):
    return db.fetch_one('SELECT * FROM userInfo WHERE user_name=%s OR email=%s', [identifier, identifier])

def get_user_role(user_nore):
    return db.fetch_one('SELECT role FROM userInfo WHERE user_name=%s OR email=%s', [user_nore, user_nore])

def insert_user_info(username,email,password):
    return db.implement('INSERT INTO userInfo(email,password,user_name) VALUES(%s,%s,%s)',
                 [email, password, username])
