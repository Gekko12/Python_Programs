"""
Bubble sort:
It is so called because elements tend to move up into the correct order like bubbles rising to the surface.
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in
wrong order.

Initialize var2 as number of elements in the list
for (var1=0, var1<var2-1, var1=var1+1)
     a. Initialize swapped as False
     b. for (var3=0, var3<var2-var1-1, var3=var3+1)
          i. if list[var3] > list[var3+1] then
          Swap the elements at positions var3 and var3+1
          Change the value of swapped to True
     c. if (swapped==False) then break

Example:
First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole
pass without any swap to know it is sorted.

Third Pass:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.
Sorting In Place: Yes
Stable: Yes

Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm.
In computer graphics it is popular for its capability to detect a very small error (like swap of just two elements) in
almost-sorted arrays and fix it with just linear complexity (2n). For example, it is used in a polygon filling
algorithm, where bounding lines are sorted by their x coordinate at a specific scan line (a line parallel to x axis)
and with incrementing y their order changes (two elements are swapped) only at intersections of two lines
(Source: Wikipedia)
"""


def swap(num_list, first_index, second_index):
    """
    To swap two elements from list using their indices
    """
    global no_of_swaps
    temp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = temp
    no_of_swaps += 1


def bubble_sort(num_list):
    """
    Implementation of bubble sort
    """
    global no_of_passes
    end_index = len(num_list)
    for index1 in range(0, end_index - 1):
        swapped = False
        no_of_passes += 1
        for index2 in range(0, (end_index - index1 - 1)):
            if num_list[index2] > num_list[index2 + 1]:
                swap(num_list, index2, index2 + 1)
                swapped = True
        if not swapped:
            break
        print("At the end of pass-", no_of_passes, ":", num_list)


no_of_swaps = 0
no_of_passes = 0
num_l = [5, 4, 3, 2, 1]
print("In the beginning:", num_l)
print("______________________________________________")
bubble_sort(num_l)
print("______________________________________________")
print("At the end:", num_l)
print("______________________________________________")
print("No. of swaps:", no_of_swaps)
print("No. of passes:", no_of_passes)
