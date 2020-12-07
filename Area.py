# Program to print the area of circle ,rectangle  and sq.

import math

def area_cir( rad ) :			#rad for radius of circle
	return (math.pi * rad * rad) 		#math.pi  is inbuilt data variable

def area_rec( lengh , breadth ) :
	return (length * breadth)
	
def area_sq( length ) :
	return (length * length)
	
while( True) :
	print('''------------------------------- Menu -------------------------------
	1. Area of circle
	2. Area of rectangle
	3. Area of Square	
	4. Quit			''')

	choice = int(input("\nEnter your choice :"))

	if choice == 1 :
		rad = float(input("Enter radius of circle :"))
		print('Area = ', area_cir(rad))
	elif choice == 2 :
		length = float(input("Enter length of rectangle :"))
		bdh = float(input("Enter breadth of rectangle :"))
		print('Area =', area_rec(length ,bdh))
	elif choice == 3 :
		length = float(input("Enter length of Square :"))
		print('Area =', area_sq(length))
	elif choice == 4 :
		exit(0)		#exit(0) indicates normal termination
	else	:
		print("\nWrong input.......Terminating .......\n")
		exit()	#bydefault exit() takes 0 as args ie. normal termination bydefault

quit()	#quit() used for program termination while exit() used for loop termination
