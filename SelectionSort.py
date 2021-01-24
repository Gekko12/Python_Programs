"""
*** Python can compute 10^7 steps in 1 second ...we can see this while executing a python file in
    terminal using "time " cmd
    $time python3 SelectionSort.py


Selection Sort algorithm ,works by finding the smallest element in a list and replacing
the first element from a list .... (| indicates the sorted list)

45 | 67 54 96 5 98      #find the smallest element in a list and swap with the first element
^           ^
5 67 | 54 96 45 98
  ^          ^
5 45 54 | 96 67 98
     ^^
5 45 54 96 | 67 98
        ^    ^
5 45 54 67 96 | 98
           ^^
5 45 54 67 96 98 |

Time Complexity :-  O(N^2)
T(N) = N + (N-1) + (N-2) + ..... + 1 = N(N+1)/2 = O(N^2)
As scan reduces every time by 1 ..... and sum of N natural numbers are n(n+1)/2

"""


def SelectionSort(lst):
    """
    SelectionSort() algorithm implementation
    :param lst: list of all inputed elements
    :return: returns the sorted list in Ascending order
    """

    for i in range(len(lst) - 1):
        ele = lst[i]
        minval = ele
        swap_pos = i

        for j in range(i, len(lst)):
            if lst[j] < minval:
                minval = lst[j]
                swap_pos = j

        (lst[i], lst[swap_pos]) = (minval, ele)

    return lst


# main-function
list_ = list(map(int, input("Enter list :").strip().split()))

print("Sorted list :-")
print(SelectionSort(list_))

quit(0)
