# power of 2

def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n - 1)
        return power * 2


print(powerOfTwo(5))


# factorial

# def factorial(n):
#     # if n == 0 or n == 1:
#     assert n >= 0 and int(n) == n, 'the number must be positive integer'
#     if n in [0, 1]:
#         return 1
#     else:
#         fact = n * factorial(n - 1)
#         return fact


# print(factorial(-1))


# fibonacci series
def fibonacci(n):
    assert n >= 0 and int(n) == n , 'fibonacci number cannot be negative'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
