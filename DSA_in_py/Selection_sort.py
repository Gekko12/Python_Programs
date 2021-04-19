"""
Selection sort:
It is so called because it selects the smallest/largest element in the list and swaps it with the element at the first
position, then selects the next smallest/largest element in the list and swaps it with the element at the second
position and so on until it is done with the number at last position in the list.

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is
picked and moved to the sorted subarray.

Following example explains the above steps:

arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
11 12 22 25 64

Time complexity -
Worst complexity: O(n^2)
Average complexity: O(n^2)
Best complexity: O(n^2)
Space complexity: 1

Auxiliary Space: O(1)
In Place : Yes, it does not require extra space.
Stable : Can be achieved

The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is
a costly operation.
"""


def swap(num_list, first_index, second_index):
    """
    This function swaps the elements from a list with given indices
    """
    num_list[first_index], num_list[second_index] = num_list[second_index], num_list[first_index]


def find_next_min(num_list, start_index):
    """
    It finds the next minimum element from a list starting from start index
    """
    min_ = num_list[start_index]
    index = start_index
    for i in range(start_index, len(num_list)):
        if num_list[i] < min_:
            min_ = num_list[i]
            index = i
    return index


def selection_sort(num_list):
    """
    Implementation of selection sort
    """
    for i in range(0, len(num_list)):
        small_index = find_next_min(num_list, i)
        swap(num_list, i, small_index)


num_l = [8, 2, 19, 34, 23, 67, 91]
print("Before sorting;", num_l)
selection_sort(num_l)
print("After sorting:", num_l)
