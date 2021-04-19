"""
                        --- Quick Sort ---

This sorting strategy known as Quick Sort works by picking an element in the input list as pivot and partitioning the
list around the pivot. Partitioning is done such that :
    - the pivot is placed at its correct position in the list,
    - elements less than pivot are placed in the left partition and
    - elements greater than the pivot are kept in the right partition.
This is repeatedly done for each partition until all pivots are correctly placed in the list.

The detailed algorithm is as follows:
    quick_sort(list, low, high):
        1. If low>=high then return
        2. p=Partition(list, low, high)
        3. Invoke Quick_Sort() by passing list, low and p-1
        4. Invoke Quick_Sort() by passing list, p+1, high

    partition(list, low, high):
        1. Choose the element at position low as the pivot
        2. Initialize i as low+1 and j as high
        3. Initialize done as False
        4. While not done do
            a. While (i<=j) and list[i]<=pivot) do increment i by 1
            b. While (j>=i) and list[j]>=pivot) do decrement j by 1
            c. If (j < i) then change the value of done to true
            d. Else swap the elements at position i and j
        5. Swap the elements at position j and low
        6. Return the partition point, j

In the quick sort algorithm we implemented, we have considered pivot as the first element.
However, pivot can also be:
    - A random element in the list.
    - First, middle or the last element in the list
    - Median of first, middle and last element values in the list (“median-of-three”)

Time complexity:
    Best: O(n log(n))
    Average: O(n log(n))
    Worst: O(n * n)
"""


def swap(num_list, first_index, second_index):
    """
    To swap the list elements at position first_index and second_index
    """
    temp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = temp


def quick_sort(num_list, low, high):
    """
    To implement quick sort
    """
    if low >= high:
        return
    split_point = partition(num_list, low, high)
    quick_sort(num_list, low, split_point - 1)
    quick_sort(num_list, split_point + 1, high)


def partition(num_list, low, high):
    """
    To partition the num_list and returns the partition point
    """
    pivot = num_list[low]
    i = low + 1
    j = high
    done = False
    while not done:
        while i <= j and num_list[i] <= pivot:
            i += 1
        while num_list[j] >= pivot and j >= i:
            j -= 1
        if j < i:
            done = True
        else:
            swap(num_list, i, j)
    swap(num_list, low, j)
    return j


n_list = [3, 1, 0, 4, 2]
print("Before sorting;", n_list)
len_ = len(n_list)
quick_sort(n_list, 0, len_ - 1)
print("After sorting:", n_list)