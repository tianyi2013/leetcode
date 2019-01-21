def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    i = 0
    while True:
        if i * i <= x < (i + 1) * (i + 1):
            return i
        i += 1


def sqrtBinarySearch(x):
    left, right = 1, x
    while True:
        middle = int((left + right) / 2)
        if middle * middle <= x < (middle + 1) * (middle + 1):
            return middle
        elif middle * middle > x:
            right = middle
        else:
            left = middle


#print(mySqrt(2015628227))
print(sqrtBinarySearch(2015628227))
