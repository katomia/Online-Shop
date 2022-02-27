from os import read
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
with open('./create.sql','r',encoding='UTF-8') as f:
	s=f.read()
	c.executescript(s)

conn.commit()
conn.close()