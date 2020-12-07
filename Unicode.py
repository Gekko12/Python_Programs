'''     ord() function returns a unicode value of char and unicode already follows ASCII
        chr() function is just opposite to ord() ie. if chr(65) gives 'A'
'''

str1 = input("Enter a single character to find the unicode(ASCII)  value of it : ")

try :
        val = ord(str1)
        print(str1,"=",val)
except :
        print("Only single character allowed ......")
