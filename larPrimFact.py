# Program to find the largest prime factor of a number

'''
Largest Prime factor of 600851475143 is 6857 
Largest Prime factor of 13195 is 29 
'''

fhand = open('Prime_Numbers.txt') #contains prime numbers upto 1 million = 10^6 = 10 lakhs

x = int(input('----------Largest Prime Factor------------\nEnter the number :'))
#x = 600851475143
temp = x
larPfact = 2
in_loop_off = False

for line in fhand :
	prime_lst = line.split()
	for y in prime_lst :
		if (x % int(y) == 0) :
			x /= int(y)
			larPfact = int(y)
		elif (x == 1) :
			in_loop_off = True
		
	if in_loop_off : break
#loops end

print('Largest Prime factor of',temp,'is',larPfact,'\n')
quit()
	 
