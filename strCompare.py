# String comparison in Python ie. check the dictionary order of a string and Capitalized words come before than non-capitalized

str1 = input("Enter 1st string :")
str2 = input("Enter 2nd string :")

if str1 < str2 :
        print(str1,"comes before",str2)
elif str1 > str2 :
        print(str1,"comes after",str2)
elif str1 == str2  :
        print(str1,"same",str2)
else :
        assert False  # When this stmt. run it will throw runtime error
