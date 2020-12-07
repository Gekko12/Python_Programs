'''
	A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 
	9009 = 91 × 99.
	Find the largest palindrome made from the product of two 3-digit numbers.
'''

def palindrome(num) :
	temp = num
	rev = 0
	
	while temp != 0 :
		digi = (int)(temp % 10)
		rev = (int)(rev*10 + digi)
		temp = temp//10			#Remeber that '/' means float division
	
	print('Num = ',num ,'and Rev = ',rev)
	if rev == num : return True
	else : return False
#end-of-def

larPro = 1
for x in range(100 ,1000) :
	for y in range(100 ,1000) :
		prod =int(x * y)
		if palindrome(prod) and (larPro < prod) : larPro = prod
#end-of-loop

print('Largest palindrome made from the product of two 3-digit numbers is ',larPro,'\n')
quit()

