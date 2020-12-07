'''
	BeautifulSoup is used for web crawling , web mining , web spidering etc
	
	For example .........
	Enter the url :-
	http://www.dr-chuck.com/
	
	After that we will get all url links for that web page which are diversing
'''

import urllib.request ,urllib.parse ,urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL(Secure Socket Layer) certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL : ')
html = urllib.request.urlopen(url, context=ctx ).read()
soup = BeautifulSoup(html ,'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags :
	print(tag.get('href' ,None))
	
quit()
