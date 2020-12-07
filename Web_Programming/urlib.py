''' 
	Since HTTP is so common, we have a lib that does all the socket work for us and makes web pages look like a file .
	
'''

import urllib.request, urllib.parse , urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand :
	print(line.decode().strip())
	
quit()
