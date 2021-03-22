'''
Program for Armstrong number like 
321 = 3^3 + 2^3 + 1^3
407 = 4^3 + 0^3 + 7^3
9474 = 9^4 + 4^4 + 7^4 + 4^4
'''


def armstrong(num):
	temp = num
	sum_ = 0
	pow_ = len(str(num))

	while temp != 0:
		rem = temp % 10
		sum_ += rem ** pow_
		temp //= 10
	
	if num == sum_ :
		print(f'%d is a armstrong number .' %num)
		return True
	
	print("{0} is not a armstrong number .".format(num))
	return False

def armGen(digit):
	arm_num_lst = list()
	from_ = int(float('1e' + str(digit-1)))	
	to = int(float('1e' + str(digit)))
	
	for x in range(from_, to):
		if armstrong(x):
			arm_num_lst.append(x)
			
	if not len(arm_num_lst):
		print("\nNone of the {} digit Armstrong number found".format(digit))	
	else:
		print("\n{} digit Armstrong numbers are :-".format(digit))
		print(arm_num_lst)



def main():
	responce = armstrong(int(input("Enter a number :")))
	digit = int(input("Enter the number of digits Armstrong number you want :"))
	armGen(digit)
	
		
		
if __name__ == "__main__":
	main()


