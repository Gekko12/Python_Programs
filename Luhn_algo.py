"""
Steps involved in Luhn algorithm ;-
A credit card has 16 digits and it can be validated using Luhn algorithm as follows-

Let’s understand the algorithm with an example:
Consider the example of an account number “79927398713“.
Step 1 – Starting from the rightmost digit double the value of every second digit,
[1, 8, 3, 2, 9] now doubles up [2, 16, 9, 4, 18]

Step 2 – If doubling of a number results in a two digits number i.e greater than 9(e.g., 6 × 2 = 12),
then add the digits of the product (e.g., 12: 1 + 2 = 3, 15: 1 + 5 = 6), to get a single digit number.

Step 3 – Now take the sum of all the digits.
ie. sum([2, 7, 9, 4, 9]) = 31

Step 4 - Now sums up the remaining digits of the credit card ie. 3, 7, 9, 7, 9, 7
3+7+9+7+9+7 = 42

Step 5 – If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according
to the Luhn formula; else it is not valid.
ie. (31 + 42) % 10 != 0. So, not a valid Luhn number.

"""


def validate_credit_card_number(card_num):
    """
    Validating credit card number using Luhn algorithm.
    """
    second_digit_starts_from_last = []
    doubled_second_digits = []
    sum_doubled_digits = []
    remaining_digits = []

    for i in range(len(str(card_num)) - 2, -1, -2):
        second_digit_starts_from_last.append(int(str(card_num)[i]))
    print(second_digit_starts_from_last)

    for i in range(0, len(second_digit_starts_from_last)):
        doubled_second_digits.append(second_digit_starts_from_last[i] * 2)
    print(doubled_second_digits)

    for i in range(0, len(doubled_second_digits)):
        if len(str(doubled_second_digits[i])) == 2:
            num = int(str(doubled_second_digits[i])[0]) + int(str(doubled_second_digits[i])[1])
            sum_doubled_digits.append(num)
        else:
            sum_doubled_digits.append(doubled_second_digits[i])
    print(sum_doubled_digits)

    for i in range(len(str(card_num)) - 1, -1, -2):
        remaining_digits.append(int(str(card_num)[i]))
    print(remaining_digits)

    total_sum = sum(remaining_digits) + sum(sum_doubled_digits)
    print(total_sum)

    if total_sum % 10 == 0:
        return True
    return False


card_number = 1456734512345698  # 4539869650133101  #1456734512345698 # #5239512608615007
result = validate_credit_card_number(card_number)
if result:
    print("credit card number is valid")
else:
    print("credit card number is invalid")
