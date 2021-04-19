"""
        ---------- Merge sort ----------

Conceptually, a merge sort works as follows:
    1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered
       sorted).
    2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be
       the sorted list.

Time complexity:
    Best: O(n log(n))
    Average: O(n log(n))
    Worst: O(n log(n))
"""


def merge(num_list, low, mid, high):
    """
    This function merge the list
    """
    i, j, k, n1, n2 = (0, 0, low, mid - low + 1, high - mid)
    left_list = num_list[low:n1+low]
    right_list = num_list[mid + 1:n2+mid+1]

    while i < n1 and j < n2:
        if left_list[i] <= right_list[j]:
            num_list[k] = left_list[i]
            i += 1
        else:
            num_list[k] = right_list[j]
            j += 1
        k += 1

    while i < n1:
        num_list[k] = left_list[i]
        i += 1
        k += 1

    while j < n2:
        num_list[k] = right_list[j]
        j += 1
        k += 1


def merge_sort(num_list, low, high):
    """
    This function divides the list till a single element is left
    """
    if low < high:
        mid = (low + high) // 2
        merge_sort(num_list, low, mid)
        merge_sort(num_list, mid + 1, high)
        merge(num_list, low, mid, high)


def main():
    """
    main-function
    """
    n = int(input("Enter the size of list : "))
    print("Enter", n, "elements of a list : ")
    num_l = list(map(int, input().strip().split()))[:n]
    print('Before sorting :', num_l)

    merge_sort(num_l, 0, n-1)
    print('After sorting :', num_l)


if __name__ == '__main__':
    main()
