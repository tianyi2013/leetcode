def add_binary(a, b):
    if len(a) < len(b):
        a = a.zfill(len(b))
    elif len(b) < len(a):
        b = b.zfill(len(a))

    carry = 0
    result = ''
    for char_a, char_b in zip(reversed(a), reversed(b)):
        int_a = int(char_a)
        int_b = int(char_b)
        if int_a + int_b + carry == 2:
            result += '0'
            carry = 1
        elif int_a + int_b + carry == 3:
            result += '1'
            carry = 1
        else:
            result += str(int_a + int_b + carry)
            carry = 0
    if carry == 1:
        result += '1'

    return ''.join(reversed(result))


#print(add_binary('1111', '1111'))


a = [1, 2, 3, 4]
print(a[-1])
