'''
        Extract all the numbers in the file and compute the sum of the numbers. 
        file_name =  regexFile.txt
'''



import re               # importing regular expression

file_name = input("Enter file name :")
handle = open(file_name)

print("\nThis program extract the numbers in a file and sum up them \n")
sum_ = 0
for line in handle :
        lst = re.findall('[0-9]+' ,line)
        if  len(lst) != 0 :
                for num in lst :
                        sum_ += int(num)

print("Sum = ",sum_)
print("\n")

exit()


