# Program for string manipulation ...Remember that this function pass a copy original no change

str1 = input("Enter a string : ")

print("\nLower-case of string = ",str1.lower()) # str1 doesn't change but pass a copy of changed str ...apply to all below function
print("Upper-case of string = ",str1.upper()) 

print("\nString slice str[4:8] = ",str1[4:8]) # from indx=4 to indx=8-1 it print the string

print("\nIs-alnum = ",str1.isalnum())

print("\nCapitalize = ",str1.capitalize()) # makes very-first alphabet capital and all lower

str2 = input("\nEnter what you want to find in above entered string : ")
print("Find = ",str1.find(str2)) # return index of occurence of very first substr in str ...if not found then -1

str3 = input("\nEnter what you want to replace : ")
str4 = input("To whom (new data) : ")
print("Replace = ",str1.replace(str3 ,str4))

print("Remove white-spaces = ",str1.strip()) # lstrip() remove WS from left ,rstrip() remove WS from right and strip() follow both

print("Starts with ...Hello = ",str1.startswith("Hello"))
 
