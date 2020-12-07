'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()

for line in handle :
        words = line.strip().split()
        
        if len(words) < 1 : continue
        if words[0] != "From" : continue
        
        time = words[5].split(':')      # To split the time format and pull out the hour from it
        hour = time[0]
        
        di[hour] = di.get(hour ,0) +1  # Add to dictionary


lst = list()        # Create a list
for key,val in di.items() :
        lst.append((key ,val))          # Store tuples in the list
        
lst = sorted(lst)               #Sort tuples in the list 
for k ,v in lst :
        print( k ,v)
        
        
