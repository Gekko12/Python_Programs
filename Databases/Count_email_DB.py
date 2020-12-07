'''
	 This application will read the mailbox data (mbox.txt) and count the number of email messages per 
 	 organization (i.e. domain name of the email address) using a database with the following schema to 
 	 maintain the counts.

						CREATE TABLE Counts (org TEXT, count INTEGER)
'''

import sqlite3 as sql
import re

conn = sql.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
#cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter file name :')
if(len(fname)<1) : fname = 'mbox-short.txt'
fh = open(fname)

for line in fh :
	if not line.startswith('From: '):continue
	pieces = line.split()
	email = str(pieces[1])
	place = int(email.find('@')) +1		#gaurav@gmail.com as we want only gmail.com
	org = email[place:].strip()
	
	cur.execute('SELECT count FROM Counts where org = ?',(org,))
	row = cur.fetchone()
	if row is None :
		cur.execute('INSERT INTO Counts(org ,count) VALUES(? ,1)',(org,))
	else :
		cur.execute('UPDATE Counts SET count = count +1 WHERE org = ?',(org,))
				
sqlstr = 'SELECT org ,count FROM Counts ORDER BY count DESC'
conn.commit()

for row in cur.execute(sqlstr) :
	print(str(row[0]) ,row[1])

cur.close()
quit()
