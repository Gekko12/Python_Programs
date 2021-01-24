"""
Insertion Sort Algorithm :-
    1. Start building a sorted sequence with one element
    2. Pickup up next unsorted element and insert it into its correct place in the already sorted
       sequence swap elements till we find the correct pos

45 | 56 23 98       (*) position it check for
*    ^
45 56 | 23 98
*  *    ^
23 45 56 | 98
      *    ^
23 45 56 98

Time Complexity : O(N^2)
Faster than Selection sort if list is already sorted
"""


def insertionSort(lst):
    """
    Insertion Sort Algorithm implementation
    :param lst: lst of input values
    :return: returns the sorted list in Ascending order
    """

    for sortedEnd in range(len(lst)):
        pos = sortedEnd
        while pos > 0 and lst[pos] < lst[pos - 1]:
            (lst[pos], lst[pos - 1]) = (lst[pos - 1], lst[pos])
            pos -= 1

    return lst


# main-function
lst_ = list(map(int, input("Enter the list :").strip().split()))

print("Sorted list :")
print(insertionSort(lst_))

quit(0)
