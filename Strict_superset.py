"""
A strict superset has at least one element that does not exist in its subset.
Eg.
Sample Input 0
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 0
False

Explanation 0
Set A is the strict superset of the set {1, 2, 3, 4, 5} but not of the set {100, 11, 12} because 100 is not in set A.
Hence, the output is False.
"""

set_a = set(map(int, input("Input Set A : ").strip().split()))
n = int(input("Input n: "))
res = True

while n:
    set_sub = set(map(int, input("Input Set B{} : ".format(n)).strip().split()))
    n -= 1
    if res:
        intersection = set_a & set_sub
        if (intersection != set_sub) or (len(set_a) <= len(set_sub)):
            res = False

if not res:     # if all subsets doesn't follow the strict superset then False else True
    print('{} :- Set A is not a strict superset of Set B.'.format(res))
else:
    print('{} :- Set A is a strict superset of Set B.'.format(res))