import sqlite3

conn = sqlite3.connect('login.db')
c = conn.cursor()
c.execute("""
CREATE TABLE LOGIN(name text,password text)
""")
c.execute("""
CREATE TABLE appdigitcode(password text)
""")
conn.commit()
conn.close()