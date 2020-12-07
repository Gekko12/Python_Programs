#JSON  - 	JavaScript Object Notation

import json

#It's simpler than XML and looks like a dictionary and use double qoutes only
data = ''' {
	"name" : "Gaurav",	
	"phone" : "+91 80548956"
} '''
		

info = json.loads(data)	#info is a  list produced by parsing JSON 
print( "Length : ",len(info))

print("Name : ",info["name"])
print("Phone : ",info["phone"])

quit()

	
