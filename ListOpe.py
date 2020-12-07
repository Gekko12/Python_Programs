'''
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at at position e
print: Print the list.
remove e: Delete the first occurrence of integer e
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list. 

Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

'''
n = int(input("Enter number of operatons :"))
res = list()

print('''\ninsert i e: Insert integer e at at position e 
print: Print the list. 
remove e: Delete the first occurrence of integer e 
append e: Insert integer e at the end of the list. 
sort: Sort the list. 
pop: Pop the last element from the list. 
reverse: Reverse the list. ''')

print("\nEnter operation and it's attributes :")
while n > 0 :
    n -= 1
    lst = list(map(str ,input().split()))

    if lst[0] == 'insert' :
        indx = int(lst[1])
        ele = int(lst[2])
        res.insert(indx ,ele)
    elif lst[0] == 'print' :
        print(res)
    elif lst[0] == 'remove' :
        ele = int(lst[1])
        res.remove(ele)
    elif lst[0] == 'append' :
        ele = int(lst[1])
        res.append(ele)
    elif lst[0] == 'sort' :
        res.sort()
    elif lst[0] == 'pop' :
        res.pop()
    elif lst[0] == 'reverse' :
        res.reverse()
    else :
        assert False

