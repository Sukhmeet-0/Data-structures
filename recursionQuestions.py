# sum of digits in a number
def sumOfDigits(n):
    assert 0 <= n == int(n), "Number must be positive"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(n // 10)


print(sumOfDigits(5615))


# calculate power of number
def powerOfNumber(base, exp):
    # assert exp >= 0 and int(exp == 0), 'the exponent must be positive integer'
    # assert base >= 0 and int(base == 0), 'the base must be positive integer'
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base * powerOfNumber(base, exp - 1)


print(powerOfNumber(2, 4))


# GCD
def GCD(a, b):
    assert int(a) == a and int(b) == b, 'the integers must be positive'
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


print(GCD(48, -18))


# decimal to binary
def decimalToBinary(n):
    assert int(n) == n, 'the parameter must be integer only'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n / 2))


print(decimalToBinary(13))
