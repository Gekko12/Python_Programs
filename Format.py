'''
	" {0} {1} {2}               {N-1} ".format(arg1 ,arg2 ,arg3 ....... ,argN)
'''

age = int(input("Enter your age : "))
name = input("Enter your name : ")

coll = input("Enter your collage name : ")

wel_msg = '\n{} {} to the world of programming '.format("Welcome" ,name)

detail = '\nYou are {0} years old .....you know {1} years old HomoSapiens is known for \" Energy \" '.format(age ,'18')

print(wel_msg + '\n' + detail)
print('''\nDetails :-
		Name = {0}
		Collage = {2}
		Age = {1}
		\n\n'''.format(name ,age ,coll) )
		

