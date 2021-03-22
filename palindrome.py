''' Program for palindrome of a number like 121, 1331, 2332,78900987,123456654321 etc. 
'''


def palindrome(num):
	temp = num
	rev = 0
	
	while temp != 0:
		rem = temp % 10
		rev = rev*10 + rem
		#print(rem, rev, temp)
		temp //= 10				#don't forget integer division .... otherwise result will be different
	if rev == num:
		print('{} is a palinddrome'.format(num))
	else:
		print(f'%d is not a palindrome'%num)


def main():
	n = int(input("Enter a number :\n")) ;		#see we can write : (semi-colon) also in python
	palindrome(n)


if __name__ == "__main__":
	main()
		
