"""
Program for Binary Search impletation ......
Binary serch accepts data in order form .... be careful
Time complexity :-  O(logN)
T(0) = 1
T(N) = 1 + T(N/2)           [as we dividing list each time by half]
     = 1 + 1 + T(N/(2^2))
     = 1 + 1 + 1 ...(K TIMES)... + 1 +T(N/(2^K))        [2^K = N  so , K = log2(N)] ->(1)
     = K + T(N/(2^log2(N))                          [sunstituting eq. (1) ]
     = log2(N) + T(N/N)
     = log2(N) + 1
     = O(log2(N))
"""


def BinSearch(l, key1):
    """
    BinSearch() returns index of the element if got ,else -1
    :param l:   list
    :param key1:    key to find
    :return:    return index of key ...if not present then -1 as indx
    """
    low = 0
    high = len(l) - 1
    mid = (low + high) // 2
    indx1 = -1

    while low <= high:
        if l[mid] == key1:
            indx1 = mid
            break
        elif key1 < l[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = (high + low) // 2

    return indx1


def InputOrder(nele, l):
    """
    InputOrder() to take input in order form if not return a msg
    :param nele:    number of elements
    :param l:   list
    :return:    return True if list is ordered else False
    """
    print("Enter elements in order form(Ascending) :")
    l[:] = list(map(int, input().strip().split()))[:nele]
    # without lst[:] splicing outer scopr lst is not in effect as ....[:n] splicing generates new list
    asc = False

    if len(l) != nele:
        print("Invalid list insertion .....list size not satisfied")
        return False

    if len(l) <= 1:
        return True

    for i in range(nele - 1):
        if l[i] <= l[i + 1]:
            asc = True
        else:
            asc = False
            break

    if asc:
        print("Ordered input .....Proceeding.....")
        return True

    print("Not an ordered input...........Terminating  :(")
    return False


# main-function
n = int(input("Enter number of elements :"))
lst = []  # empty list where input stores

msg = InputOrder(n, lst)
if not msg:
    exit(0)

print(lst)
key = int(input("Enter the key to look up :"))

indx = BinSearch(lst, key)
if indx == -1:
    print("Invalid key")
else:
    print("Key=", key, "found at index=", indx)

quit(0)
