""" Program to count the of words  in a file romeo.txt and to get the largest count """

file_name = input("Enter file name : ")

file = open(file_name)          # By default open() will take argument as read

di = dict()

for line in file :                      # It will take line by line
        words = line.strip().split()            # To remove spaces and to split a line into words
        for wo in words :
                di[wo] = di.get(wo ,0) + 1
 
            
bigCount = None
bigWord = None

for key,val in di.items() :
        if bigCount is None or val > bigCount :
                bigCount = val
                bigWord = key
                
print(bigWord,"has a largest count of ",bigCount,"\n")     
 
