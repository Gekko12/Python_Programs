# Program to show parsing and extracting 

print("\nTo extract the email  from a string  ")
str1 = input("\nEnter a string : ")

at_rate = str1.find('@gmail.com')

len_gmail = len('@gmail.com')

substr = str1[ : at_rate+len_gmail]

print("Email_ID = " ,end=" ")

i = at_rate
while i > 0 :
        if substr[i] == " " :
                break
        i -= 1

print(substr[ i+1: at_rate+len_gmail+1])

