"""
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
"""


def is_happy(n):
    sums = []

    def sqr_sum(number):
        sum = 0
        for digit in str(number):
            sum += int(digit) ** 2
        return sum

    while n != 1:
        n = sqr_sum(n)
        if n in sums:
            return False
        else:
            sums.append(n)

    return True


print(is_happy(19))
print(is_happy(2))
