"""
Python doesn't have built-in stack , but can be implemented using list
"""


class Stack:
    """
    Stack class has push and pop operation, mainly
    """

    def __init__(self, max_size=10):
        self.__max_size = max_size  # Stack's max-size
        self.__top = -1
        self.__elements = [None] * max_size  # making a list of [None, None....]

    def get_max_size(self):
        """
        Returns max_size of a stack
        """
        return self.__max_size

    def get_top(self):
        """
        Returns top of a stack
        """
        return self.__top

    def is_empty(self):
        """
        Returns true if top==-1 ie. stack underflow
        """
        if self.__top < 0:
            return True
        return False

    def is_full(self):
        """
        Returns true if top >= max_size ie. overflow
        """
        if self.__top >= self.__max_size-1:
            return True
        return False

    def push(self, data):
        """
        Push data to the top of stack
        """
        if not self.is_full():
            self.__top += 1
            self.__elements[self.__top] = data
        else:
            print('Stack Overflow .......')

    def pop(self):
        """
        Pop out the top-most of element
        """
        if not self.is_empty():
            data = self.__elements[self.__top]
            self.__elements[self.__top] = None
            self.__top -= 1
            return data
        return 'Stack underflow ......'

    def display(self):
        """
        Display the stack element from top to bottom
        """
        n_sp = 20
        space = '_'
        print('Stack from top to bottom :-\n')
        if self.is_empty():
            print('|', space * n_sp, '|', sep='')
        else:
            index = self.get_top()
            while index > -1:
                ele = self.__elements[index]
                index -= 1
                st = str(ele).center(20, '_')
                print('|', st, '|', sep='')


def main():
    """
    main-function
    """
    s = Stack(3)
    print('pop():', s.pop())

    print('push(): 126')
    s.push(126)
    print('push(): 52')
    s.push(52)
    print('push(): 958')
    s.push(958)

    s.display()
    print('push(): 325')
    s.push(325)

    print('pop():', s.pop())
    s.display()


if __name__ == '__main__':
    main()
