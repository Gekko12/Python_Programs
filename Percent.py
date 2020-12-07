'''
Display the percentage of query student by calculating marks of 3 subjects in 2 decimal digits .
 
Sample Input 
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 
56.00

Explanation 
Marks for Malika are {52,56,60} whose average is (52+56+60)/3 = 56.00
''' 


#Program
n = int(input("Enter number of students :"))

print("Enter Student name and marks in three subjects respectively in a single line :")

try :
        di = dict()
        for i in range(n) :
            lst = list(map(str ,input().strip().split()))
            name = lst.pop(0)
            su = 0
            for x in range(3) :
                su += float(lst[x])
            
            su = su / 3.0
            di[name] = di.get(name ,su)

        query = input("Enter student name whom you want to query percentage scored :")
        res = di.get(query)
        print('Percentage scored = %.2f'%res)

except :
        print("WRONG insertion ..... input name and marks in a single line for each student.....\n") 
