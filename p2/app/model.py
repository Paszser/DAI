from pickleshare import *

db = PickleShareDB('~/testpickleshare')
db.clear()

def login_bd_email(email):
    return email in db.keys()

def login_bd_password(email,password):
    return password == db[email]

def add_user(email,password):
    db[email] = password
    return None