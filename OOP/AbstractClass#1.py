from abc import ABCMeta, abstractmethod
"""
abstract classes are classes that have abstract methods or maybe regular methods,
but abstract methods should be implemented in child class. Abstract methods are methods which
doesn't contain implementation but only declaration

from abc import ABCMeta, abstractmethod
abc stands for Abstract Base Class, python doesn't contain abstract classes by default
"""

class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass


class Furniture(Product):
    def return_policy(self):
        print("Furnitures cannot be returned")


class Sofa(Furniture):
    print('Hi ...')


Sofa()
