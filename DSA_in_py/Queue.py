"""
Python has built-in queue module which has PriorityQueue, SimpleQueue, Queue and LifoQueue classes.
But we can implement it own by using list.
"""
# import queue


class Queue:
    """
    Implementing our own Queue class using list
    """
    def __init__(self, max_size=10):
        self.__max_size = max_size
        self.__front = 0
        self.__rear = -1
        self.__elements = [None]*max_size

    def get_max_size(self):
        """
        returns max_size of a stack
        """
        return self.__max_size

    def is_empty(self):
        """
        Returns true if Queue is empty, else false
        """
        if self.__front > self.__rear:
            return True
        return False

    def is_full(self):
        """
        Returns true if Queue is full, else False
        """
        if self.__rear >= self.get_max_size()-1:
            return True
        return False

    def enqueue(self, data):
        """
        To add data to the queue
        """
        if self.is_full():
            print('Queue is full ......')
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        """
        Removes the elements from first come first serve basis, don't confuse it with double ended queue
        returns the retrieved data
        """
        if self.is_empty():
            print('Queue is empty ......')
        else:
            data = self.__elements[self.__front]
            self.__elements[self.__front] = None
            self.__front += 1
            return data

    def display(self):
        """
        To print the Queue data
        """
        for i in range(self.__front, self.__rear+1):
            if i == self.__rear:
                print(self.__elements[i])
            else:
                print(self.__elements[i], '--> ', end='')


def main():
    """
    main-function
    """
    q = Queue(5)
    print('Max size of queue:', q.get_max_size())
    print('Is queue empty ? ', q.is_empty())

    print('q.enqueue(A)'); q.enqueue('A')
    print('q.enqueue(B)'); q.enqueue('B')
    print('q.enqueue(C)'); q.enqueue('C')
    print('q.enqueue(D)'); q.enqueue('D')
    print('q.enqueue(E)'); q.enqueue('E')
    print('q.enqueue(F)'); q.enqueue('F')

    print('Is queue full ? ', q.is_full())
    q.display()
    print('q.dequeue() :', q.dequeue())
    print('q.dequeue() :', q.dequeue())

    q.display()


if __name__ == '__main__':
    main()
