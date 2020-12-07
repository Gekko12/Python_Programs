'''
Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting of the first elment in l1, then the first element in l2, then the second element in l2, then the second element in l2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

Here are some examples to show how your function should work.

>>> shuffle([0,2,4],[1,3,5])
[0, 1, 2, 3, 4, 5]

>>> shuffle([0,2,4],[1])
[0, 1, 2, 4]

>>> shuffle([0],[1,3,5])
[0, 1, 3, 5]
'''


#max _function(a, b)
def max_fun(a ,b) :
        if a > b :
                return a
        return b
        
        
#Shuffle function
def shuffle(l1 ,l2) :
        new_lst = list()
        len1 = len(l1)
        len2 = len(l2)
        
        max_len = max_fun(len1 ,len2)
        
        for i in range(max_len) :
                if i < len1 :
                        new_lst.append( l1[i] )
                if i < len2 :
                        new_lst.append( l2[i] )
        
        return new_lst
        
                        
#main
n = int(input("Enter the length of list 1 :"))
l1 = list()
for i in range(n) :
        print("Enter element",i,"of list 1 :")
        ele = int(input())
        l1.append(ele)

m = int(input("Enter the length of list 2 :"))
l2 = list()
for i in range(m) :
        print("Enter element",i,"of list 2 :")
        ele = int(input())
        l2.append(ele)
       
print(shuffle(l1,l2))
           
                
