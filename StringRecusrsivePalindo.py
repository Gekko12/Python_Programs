"""
Recursive implementation of palindrome with case insensitive
Eg.
Palindrome :- Radar, madaM, abCBA
"""


def is_palindrome(word):
    """
    This function implements the string palindrome check recursively
    """
    word = word.lower()
    if len(word) <= 1:
        return True
    elif word[0] == word[len(word) - 1]:
        return is_palindrome(word[1:len(word) - 1])
    return False


def main():
    """
    main() function
    """
    result = is_palindrome(str(input("Enter a string for palindrome check : ")))
    if result:
        print("The given word is a Palindrome")
    else:
        print("The given word is not a Palindrome")


if __name__ == '__main__':
    main()
