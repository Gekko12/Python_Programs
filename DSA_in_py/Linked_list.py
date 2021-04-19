"""
Python doesn't have linked list built-in.
"""


class Node:
    """
    Node class implementation
    """

    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    def set_next(self, next_node):
        """
        This setter method will link next to the new node
        """
        self.__next = next_node

    def get_next(self):
        """
        This is a getter (accessor) method
        """
        return self.__next

    def set_data(self, data):
        """
        Used to set the data of a node
        """
        self.__data = data

    def get_data(self):
        """
        Used to get the data of a node
        """
        return self.__data


class LinkedList:
    """
    Linked list implementation
    """

    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        """
        To get the head
        """
        return self.__head

    def get_tail(self):
        """
        To get the tail
        """
        return self.__tail

    def set_head(self, head):
        """
        To set the head
        """
        self.__head = head

    def set_tail(self, tail):
        """
        To set the tail
        """
        self.__tail = tail

    def add_node(self, data):
        """
        To add a node in linked list at the end of linked list
        """
        new_node = Node(data)

        if self.get_head() is not None:
            tail = self.get_tail()
            tail.set_next(new_node)
            self.set_tail(new_node)
        else:
            self.set_head(new_node)
            self.set_tail(new_node)

    def add_node_beg(self, data):
        """
        To add a node at the beginning
        """
        new_node = Node(data)

        if self.get_head() is not None:
            head = self.get_head()
            new_node.set_next(head)
            self.set_head(new_node)
        else:
            self.set_head(new_node)
            self.set_tail(new_node)

    def remove_node(self, key):
        """
        To remove a node mentioned traversing from the starting
        """
        if self.get_head() is None:
            print('Empty Linked list')
        else:
            prev = None
            past = None
            got = False
            tmp_head = self.get_head()

            while tmp_head.get_next() is not None:
                if tmp_head.get_next().get_data() == key:
                    prev = tmp_head
                    past = tmp_head.get_next().get_next()
                    got = True
                    break
                tmp_head = tmp_head.get_next()

            if got:
                prev.set_next(past)
                print('%s removed ' % format(key))
            else:
                print('%s not found ' % format(key))

    def print_Linked_list(self):
        """
        To display the linked list
        """
        print('\nLinked list :-')
        tmp_head = self.get_head()
        while tmp_head is not None:
            data = tmp_head.get_data()
            print(data, end='')
            tmp_head = tmp_head.get_next()
            if tmp_head is not None:
                print(' -> ', end='')
        print('\n')

    def node_count(self):
        """
        To count the number of nodes
        """
        count = 0
        tmp_head = self.get_head()
        while tmp_head is not None:
            count += 1
            tmp_head = tmp_head.get_next()
        return count

    def search_node(self, key):
        """
        To search for a node in the linked list if not found return None else position with indexing 0.
        """
        pos = None
        head = self.get_head()
        index = 0

        while head is not None:
            if key == head.get_data():
                pos = index
                break
            index += 1
            head = head.get_next()
        return pos

    def insert_after_node(self, data, data_before=None):
        """
        To insert a node after data_before node, and if data_before node's data
        is not provided or data_before not found then insert at the head.
        It accepts the data in the node to be inserted and the data in the node after which the new node
        should be inserted.
        """
        node = Node(data)
        if self.search_node(data_before) is not None:
            pointer = self.get_head()
            while pointer is not None:
                if data_before == pointer.get_data():
                    # node_before = head
                    node.set_next(pointer.get_next())
                    pointer.set_next(node)
                    break
                pointer = pointer.get_next()
        else:
            self.add_node_beg(data)


def main():
    """
    main function
    """
    ll = LinkedList()

    ll.add_node('Banana')
    ll.add_node('Apple')
    ll.add_node_beg('Cat')
    ll.add_node(123)
    ll.print_Linked_list()

    ll.remove_node('Apple')
    ll.remove_node(456)

    ll.add_node('Champion')
    ll.add_node_beg('Apple')
    ll.print_Linked_list()

    print('Number of nodes = ', ll.node_count())

    print('\nCat at position :', ll.search_node('Cat'))
    print('999 at position :', ll.search_node(999))

    ll.insert_after_node('Dog', 'Cat')
    ll.insert_after_node('Head')
    ll.insert_after_node('Mouse', 'Key')
    ll.print_Linked_list()


if __name__ == '__main__':
    main()
