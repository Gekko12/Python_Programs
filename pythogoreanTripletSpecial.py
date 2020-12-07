'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


#main-function

for a in range(1 ,1000) :
	for b in range(a+1 ,1000) :
		for c in range(b+1 ,1000) :
			if (a**2 + b**2)==c**2 and (a+b+c)==1000 :
				print('Special triplets -> a=',a ,',b=',b ,',c=',c,'\n')
				exit(0) #to break the deep loops

#quit() not required

