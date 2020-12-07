'''
    input() 
This is used to fetch input from the user. In this case. We are expecting the user to provide a list of integers. How do I know? Look next.

    input().strip() 
This will eliminate trailing spaces from the user input, if they are there. Why is it required? Because some users will do that and that might break your program.

Remember that input() will cast the input as string. So, now we have a string of integers like so: “1 2 4 42”

    input.strip().split() 
split() is used to create a Python list out of a string. If no delimiter is given, this breaks the string by spaces. So, now we 
have: [“1”, “2”, “4”, “42”]

    map(int, input().strip().split()) 
map() takes two arguments. The first one is the method to apply, the second one is the data to apply it to. By this understanding, we can see this is doing nothing but typecasting every element of the list to an integer value. Since map returns the data type it was applied to, the list() method applied over map() is redundant. So now we have covered the following:

    list(map(int, input().strip().split())) 

And we have: [1, 2, 4, 42]

Note the missing quotes. This means the elements are now all int.

    list(map(int, input().strip().split()))[:I] 
takes the list we have obtained and returns only the first I elements.
'''



#Program to find second maximum from a list
n = int( input("Enter the length of list :"))

print("Enter elements  (in a single row only) : ")
lst = list(map (int ,input( ).strip().split() ))[:n]                 

lst.sort(reverse = True)        #To sort it in descending order

z = lst.pop(0)          # It will pop out the 0th index ele ie. max of list     Alternate .     We can use max()
y = lst.pop(0)
while z == y :
        y = lst.pop(0)
        #assert True             #do nothing

print("Second maximum element after removing duplicate of First maximum element : " ,y,"\n")

