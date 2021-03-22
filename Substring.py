"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring
occurs in the given string. String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.

Input Format
The first line of input contains the original string. The next line contains the substring.

Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input:
ABCDCDC
CDC

Sample Output
2
"""


def count_substring(string1, sub_string1):
    """
    string1: parent string
    sub_string1: sub string to be matched overlapping also count
    """
    count1 = 0
    sub_len = len(sub_string1)
    str_len = len(string1)

    for x in range(0, str_len - sub_len + 1):
        temp = string1[x:x + sub_len]
        if temp == sub_string1:
            count1 += 1
    return count1


if __name__ == '__main__':
    string = input("Enter a string : ").strip()
    sub_string = input("Enter a sub-string to be matched : ").strip()

    count = count_substring(string, sub_string)
    print(count)
