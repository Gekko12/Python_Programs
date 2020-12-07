import xml.etree.ElementTree as ET	#ET is an alias(short notation/reference)

#XML is very much similar to HTML , here we create a student XML
data ='''
<student>
	<uid type="int">128</uid>
	<name>Gaurav</name>
	<phone type="int">
	   +918054 166445
	</phone>
</student>
'''

tree = ET.fromstring(data)	#creates a tree mapping of data
print('Name : ',tree.find('name').text)
print('UID : ',tree.find('uid').text)
print('Phone : ',tree.find('phone').text.strip())	#As without strip it takes tabs also provided before data entering...just for beautify

quit()
