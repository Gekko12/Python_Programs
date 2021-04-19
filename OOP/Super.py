"""
super() function is used to access the base class attributes or static variables (not instance attributes) or methods.
"""


class A:
    num = 50
    val = 99

    def __init__(self):
        self.a_var = 100
        print('In constructor A')

    def show(self):
        print('In class A')

    def fun_a(self):
        print('In function A')


class B(A):
    val = 999

    def __init__(self):
        super().__init__()
        self.num = 150
        print('In constructor B')

    def show(self):
        print('In class B')
        super().show()
        print('B\'s num =', self.num)
        print('Accessing A\'s num using B.num =', B.num)
        print('A\'s num =', super().num)
        print('A\'s val =', super().val)
        print('B\'s val =', self.val)
        print('A\'s a_var using self, is', self.a_var)
        try:
            print('A\'s a_var =', super().a_var)
        except Exception as e:
            print('super() can\'t access instance attributes, but can access static var:', e)


# main - function
obj = B()
obj.show()
obj.fun_a()
print('------------ Very important ---------------------')
print('To call the base class method outside the classes using object and super')
super(type(obj), obj).show()
