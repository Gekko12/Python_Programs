"""
Private attributes are created by adding double underscore in front of attributes of a class.
They can be accessed inside a class only.
"""

class A:
    def __init__(self, uid, name, age):
        self.__id = uid
        self.name = name
        self.age = age

    def show(self):
        print('ID:', self.__id, ', Name:', self.name, ', Age:', self.age)


obj = A(101, 'ABCDEF', 25)
obj.show()
print(obj.name)
try:
    print(obj.__id)
except Exception as e:
    print('As private variable only accessed inside a class, -', e)