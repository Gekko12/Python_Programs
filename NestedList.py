# Program to input nested list and find the second highest grades of students

n = int( input("Enter the number of students :"))

lst = list()
for i in range(n) :
        lst.append([input("Enter your name :") , float(input("Enter your marks :"))])  
        print()

lst.sort()
print(lst)

n = int(input("\nEnter the N for sq. matrix :"))
lst = [ [for i in range(n)] for i in range(n)]
print(lst)

quit()
