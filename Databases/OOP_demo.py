'''	Creating a class in python
	if class A inherits all the properties of class B then in python its written like
		class A(B) :
'''

#class definition starts
class CallCount :
	x = 0
	name = ""
	
	def __init__(self ,z) :			#used for initialising object's data
		print('Constructor call by ',z)
		self.x = 1
		self.name = z
			
	def callC(self) :	#counts the number of time an method call
		print(self.name ,'called ' ,self.x ,'times')
		self.x = self.x +1
	
	def __del__(self) :
		print('Destructor call by ',self.name,'.......freeing memory.....yaaahoooo...')
#class ends
	

#main function
obj1 = CallCount("Saly")	#object of class CallCount
obj1.callC()

obj2 = CallCount('Ron')
obj2.callC()
obj2.callC()

obj1.callC()

print("\nType :",type(obj1))
print('Dir :',dir(obj1))
print()
quit()
