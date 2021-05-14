def reverse_signed(num):
    result = 0
    sign_number = 1
    if num < 0:
        sign_number = -1
        num = num * -1
    while num > 0:
        remainder = num % 10
        result = result*10 + remainder
        num = num // 10
    if not -2147483648 < result < 2147483647:
        return 0
    return sign_number *result

print(reverse_signed(123))