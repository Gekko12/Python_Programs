'''
1. Write a function contracting(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly decreases.
Here are some examples of how your function should work.
  >>> contracting([9,2,7,3,1])
  True
  >>> contracting([-2,3,7,2,-1]) 
  False
  >>> contracting([10,7,4,1])
  False
  
2. In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a hill if it is strictly greater than its neighbours and a valley if it is strictly less than its neighbours.
Write a function counthv(l) that takes as input a list of integers l and returns a list [hc,vc] where hc is the number of hills in l and vc is the number of valleys in l.
Here are some examples to show how your function should work.
>>> counthv([1,2,1,2,3,2,1])
[2, 1]
>>> counthv([1,2,3,1])
[1, 0]
>>> counthv([3,1,2,3])
[0, 1]

3. A square n×n matrix of integers can be written in Python as a list with n elements, where each element is in turn a list of n integers, representing a row of the matrix. For instance, the matrix
  1  2  3
  4  5  6
  7  8  9
would be represented as [[1,2,3], [4,5,6], [7,8,9]].
Write a function leftrotate(m) that takes a list representation m of a square matrix as input, and returns the matrix obtained by rotating the original matrix counterclockwize by 90 degrees. For instance, if we rotate the matrix above, we get
  3  6  9
  2  5  8    
  1  4  7
Your function should not modify the argument m provided to the function rotate().
Here are some examples of how your function should work.
  >>> leftrotate([[1,2],[3,4]])
  [[2, 4], [1, 3]]
  >>> leftrotate([[1,2,3],[4,5,6],[7,8,9]])
  [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
  >>> leftrotate([[1,1,1],[2,2,2],[3,3,3]])
  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
'''

#contracting(list[]) function
def contracting( lst ) :
	order_lst = list()
	len_lst = len(lst)
	
	for i in range(len_lst - 1) :
		a = lst[i]
		b = lst[i+1]
		order_lst.append(int(abs(a-b)))
	
	for i in range(len(order_lst)-1) :
		if order_lst[i] <= order_lst[i+1] :
			return False
	return True 
		
#counthv(list[]) function
def counthv( lst ) :
	len_lst = len(lst)
	
	if len_lst <= 2 :
		return ([0 ,0])	#no hills and no valleys
	
	hillc , valleyc = 0 , 0
	for i in range(1 , len_lst -1) :
		if lst[i] > lst[i-1] and lst[i] > lst[i+1] :
			hillc += 1
		elif lst[i] < lst[i-1] and lst[i] < lst[i+1] :
			valleyc += 1
	
	res = [hillc ,valleyc]
	return res

#leftrotate(list[[] ,[]]) function
def leftrotate( lst ) :
	len_lst = len(lst) 
	new_lst = list()
		
	i  = len_lst -1 
	while i >= 0 :
		j = 0
		temp = []
		while j < len_lst :
			temp.append(lst[j][i])
			j += 1
		#end while
		new_lst.append(temp)
		i  -= 1
	#end while
	return new_lst

		
#main_func
lst = list(map(int ,input('Enter the list for contracting :').strip().split()))
print(contracting(lst))

lst = list(map(int ,input('Enter the list for hill and valley count :').strip().split()))
print(counthv(lst))

n = int(input("Enter the N for sq. matrix :"))
lst = list(map(int ,input('Enter the whole list in a single line :').strip().split()))[:n*n]
new_lst = list()
for i in range(n) :
	temp = []
	for j in range(n) :
		temp.append(int(lst[i*n +j]))
	new_lst.append(temp)
	
print(new_lst)		
print(leftrotate(new_lst))

quit()
	
