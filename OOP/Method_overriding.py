"""
If a child class doesn't want to use a method inherited from parent class then it's may create
its own method with the same name
"""


class A:
    def show(self):
        print('In class A')


class B(A):
    def show(self):
        print('In class B')
        # super().show()


B().show()
