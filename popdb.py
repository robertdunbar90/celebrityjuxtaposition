import sqlite3 as lite
import sys

c = []

f = open('newdata', 'r')

for line in f:
	p = line.strip().split(':')
	p.append(1)
	p.append(1)
	c.append(p)

con = lite.connect('celebs.db')

with con:
    
    cur = con.cursor()    
    
    for line in c:
    	cur.execute("INSERT INTO questions (question, answerA, descriptionA, answerB, descriptionB, aCount, bCount) VALUES(?, ?, ?, ?, ?, ?, ?)", line)