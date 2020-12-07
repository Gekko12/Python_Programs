# Program to generate the Prime numbers and store in a file -> Prime_Numbers.txt


from SeiveOfEratosthenes import *		#program already created 

fhand = open('Prime_Numbers.txt' ,'w')
n = int(input('Enter the (upper) range for primes : '))
primes = list()
primes = Seive(n)	#Seive() returns a boolean list for primes

count20 = 1 	#to put only 20 primes in a single line
for i in range(n+1) :
	if primes[i] :
		if (count20 <= 20) :
			count20 += 1
			fhand.write(str(i)+' ')
		else :
			count20 = 1
			fhand.write('\n')
			fhand.write(str(i)+' ')
			count20 += 1
#for-loop closed
fhand.close()
quit()


