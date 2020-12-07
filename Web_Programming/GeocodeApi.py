import urllib.request ,urllib.parse ,urllib.error
import json

place_name = input("Enter a place name: ")
base_url = "http://py4e-data.dr-chuck.net/json?" #As for google API we need key and for key we need money
#using dr-chuck.net/json we can queiry 

parms = dict()
parms['address'] = place_name
parms['key'] = 42
target = base_url + urllib.parse.urlencode(parms)

print ("Retrieving {0}".format(target))
connection = urllib.request.urlopen(target)
data = connection.read().decode()
print ("Retrieved {0} characters".format(len(data)))
parsed_data = json.loads(data)



if not parsed_data or 'status' not in parsed_data or parsed_data['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        exit()
        
print (json.dumps(parsed_data ,indent=2 ))

lat = parsed_data['results'][0]['geometry']['location']['lat']
lng = parsed_data['results'][0]['geometry']['location']['lng']
print('lat', lat, 'lng', lng)

location = parsed_data['results'][0]['formatted_address']
print(location)

print ("Place id", parsed_data["results"][0]["place_id"])

quit()
