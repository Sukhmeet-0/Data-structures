# # sum and product of array
#
# def foo(array):
#     sum = 0  # -------------->O(1)
#     product = 1  # -------------->O(1)
#     for i in array:  # -------------->O(n)
#         sum += i  # -------------->O(1)
#         product *= i  # -------------->O(1)
#     print(f"Sum = {sum} \"product\" = {round(product, 2)}")  # -------------->O(1)
#
#
# s = [1, 2, 3, 45, 5, 6, 5, 4, 343, 3]  # -------------->O(1)
# ss = [1, 2, 3, 45, 5, 6, 5, 4, 343, 3]  # -------------->O(1)
# foo(s)  # -------------->O(1)
#
#
# # print pairs
#
# def printPairs(array):  # -------------->O(1)
#     for i in array:  # -------------->O(n)    -------------
#         #                                                  -------->O(n^2)
#         for j in array:  # -------------->O(n) -------------
#             print("[ ", str(i), ",", str(j), " ]", end=" ")  # -------------->O(1)
#
#
# printPairs(s)  # -------------->O(1)
# print("\n")
#
#
# # print unorderedPair
#
# def printUnorderedPair(array):  # -------------->O(1)
#     for i in range(0, len(array)):  # -------------->O(n)        ----
#         #                                                           ---------------->O(n^2)
#         for j in range(i + 1, len(array)):  # -------------->O(n) ----
#             print("[", array[i], ",", array[j], "]", end=" ")  # -------------->O(1)
#
#
# printUnorderedPair(s)
#
#
# # print unOrderArray pair 2
#
# # def printUnOrdered(s, ss):
# #     for i in range(len(s)):  # -------------------------->o(a)
# #         #                                                      ---------------->O(ab)
# #         for j in range(len(ss)):  # ---------------------->O(b)
# #             for k in range(0, 100000):  # ----------------->O(1)
# #                 print("[ " + str(s[i]) + "," + str(ss[j]) + " ]", end=" ")
#
#
# # printUnOrdered(s, ss)
#
#
# # reversing array
#
# def reverse(s):
#     for i in range(0, int(len(s) / 2)):  # -------------->O(n/2)
#         other = len(s) - i - 1  # -------------->O(1)
#         temp = s[i]  # -------------->O(1)
#         s[i] = s[other]  # -------------->O(1)
#         s[other] = s[i]  # -------------->O(1)
#     print(s)  # -------------->O(1)
#
#
# # factorial
#
# n = int(input("Enter the number to find factorial"))
#
#
# def factorial(s):  # -------------->M(n-1)
#     if s < 0:  # -------------->O(1)
#         return -1  # -------------->O(1)
#     elif s == 0:  # -------------->O(1)
#         return 1  # -------------->O(1)
#     else:
#         return s * factorial()  # -------------->M(n-1)
#
#
# # total complexity (N)
# factorial(n)


# # fibonacci series
#
# def allFib(n):
#     for i in range(n):
#         print(str(i) + ":, " + str(fib(i)))
#
#
# allFib(5)
#
#
# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)


# powers of 2

def powersOf2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOf2(int(n / 2))
        curr = prev * 2
        print(curr)
        return curr


powersOf2(50)
