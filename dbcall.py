import sqlite3
import random
import string
def random_16_digit_genrator(n):
    string_pass = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
    return string_pass
def insertintologin(username,password):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    userflag = False
    user = "user already exists"
    c.execute("SELECT name,password from login WHERE name = '{}'".format(username))
    d =c.fetchone()
    if d == None:
        userflag = True
        user = "created"
        c.execute("INSERT INTO login values('{}','{}')".format(username,password))
    print(user)
    conn.commit()
    conn.close()
    return userflag,user

def get_password(username):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    c.execute("SELECT name,password from login WHERE name = '{}'".format(username))
    d =c.fetchone()
    if d == None:
        conn.commit()
        conn.close()
        return(False,None)
    if len(d) != 0:
        conn.commit()
        conn.close()
        return(True,d[1])

def set_password(username,password):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    userflag = False
    userinfo = "user Not exist"
    c.execute("SELECT name from login WHERE name = '{}'".format(username))
    d =c.fetchone()
    if d != None:
        userflag = True
        userinfo = "password changed"
        c.execute("UPDATE login SET password = '{}' WHERE name='{}' ".format(password,username))
    conn.commit()
    conn.close()
    return(userflag,userinfo)
def create_16_digit_password(password):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("INSERT INTO appdigitcode values('{}')".format(password))
    conn.commit()
    conn.close()
def return_16_digit_password():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("SELECT password from appdigitcode")
    d =c.fetchone()
    print(d)
    conn.commit()
    conn.close()
    return(d[0])
if __name__ == '__main__':
    return_16_digit_password()
    print("done")
    print(create_16_digit_password(random_16_digit_genrator(16)))
    print(get_password("bhagyarsh")) 