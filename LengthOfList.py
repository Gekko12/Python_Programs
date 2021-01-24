"""
Program to find the length of a list (recursively)

*** Recursion depth limit of python is less than 1000 ie. after that recursion fails as it
    suspend the current function starts new and there is a limit for that suspension and it
    lies nearly 998 (default) and can be set as well

    import sys
    sys.setrecursionlimit(100000)


"""


def Length(lst):
    """
    Implementation of recursion for length of a list
    :param lst: inputed list
    :return: returns the length of a list
    """

    if not lst:  # as in python empty_seq("" ,[] or even numeric value 0) is treated as False
        return 0

    return 1 + Length(lst[1:])


def SumList(lst):
    """
    Sum of the eleemnts of a list
    :param lst: inputed list
    :return: returns the sum of the elements of the list
    """

    if lst == []:       # same as above implemented
        return 0

    return lst[0] + SumList(lst[1:])


# main-function
lst_ = list(map(int, input("Enter the list :").strip().split()))
print("Length of list =", Length(lst_))

print("Sum of list =", SumList(lst_))

quit(0)
