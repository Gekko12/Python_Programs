"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following
specifications:
    Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format
A single line containing the space separated values of
N and M.

Output Format
Output the design pattern.

Sample Input
9 27

Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------


#3-lines Solutioon using list comprehension

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
"""


def print_door(n, m):
    """
    :param n: number of columns
    :param m: number of rows
    :return: returns nothing
    """

    p = ".|."
    wel = "WELCOME"

    for i in range(n):
        if i == n // 2:
            print(wel.center(m, "-"))
        elif i < n // 2:
            p_times = 2 * i + 1
            patt = p * p_times
            print(patt.center(m, "-"))
        else:
            p_times = (n - i) * 2 - 1
            patt = p * p_times
            print(patt.center(m, "-"))

    return


# main-function
n_ = int(input("Enter N :"))
m_ = int(input("Enter M :"))

print_door(n_, m_)
quit(0)
