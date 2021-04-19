"""
Static variable or shareable attribute of a class, is a variable that defines inside a class
and changes are permanent whatever class obj is called. This are accessed by using  class name only
ie. class_name.static_var_name = value

Static methods are methods which don't have instance reference variables ie. self and decorated
by using @staticmethod. This are useful for setting and getting static variables of a class
"""


class A:
    counter = 0  # this is a static attribute of class, shared by every instance

    def __init__(self, name, age):  # this is a constructor called every time during instantiation
        self.name = name
        self.age = age
        A.counter += 1

    @staticmethod
    def show_counter():     # this is a static method
        print("Counter :", A.counter)

    def show(self):
        print("Name:", self.name, ", Age:", self.age, ", ID:", A.counter)


# main-function
A('abc', 12).show()  # first time instantiation
ob2 = A('def', 18)  # second time instantiation
ob2.show()
obj3 = A('ghi', 45)  # third time instantiation
obj3.show()

print('Number of times class A is instantiated is :')
ob2.show_counter()  # see we're calling through obj 2 but, counter is changed
