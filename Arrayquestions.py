# find missing number

# a  = sum(range(0,11))
# b = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]
# b=sum(b)
# print(f"Missing number is {a-b}")


# find pair of integers whose sum is equal to given number

# a = [2, 6, 3, 9, 11]
# n = 9
# for i in range(len(a)):
#     for j in range(1,len(a)):
#         if a[i] + a[j] == n:
#             print(a[i], a[j])



# find number in array

# import numpy as np

# a = np.array([1,2,3,45,6,4,3,2,4,5,5,3,6,7,8,7,5,4,4,33])
# n = 5
# for i in range(len(a)):
#     if a[i] == n:
#         print(f"found element {n} at index {i}")


# find max product of two integers in array

# import numpy as np
# a = np.array([1,2,3,45,6,4,3,2,4,5,5,3,6,7,8,7,5,4,4,33])
# b = a[0]*a[1]
# for i in range(len(a)):
#     for j in range(1,len(a)):
#         if a[i]*a[j]>b:
#             b=a[i]*a[j]
#             pairs = str(a[i]) +", "+ str(a[j])
# print(pairs)
# print(b)


# find if a list in unique

# a = [1,3,4,4,5,6,7,7,6,5,4,4,3,3,222,2,32,2,2,4,52,52,5,524535,98]
# c = [1,2,3,4]
# b=[]
# def isUnique(a):
#     for i in a:
#         if i in b:
#             print(i)
#             return False
#         else:
#             b.append(i)
#     return True

# print(isUnique(a))


# permutation

# def permutation(list1,list2):
#     if len(list1)!=len(list2):
#         return False
#     list1.sort()
#     list2.sort()
#     if list1 == list2:
#         return True
#     else:
#         return False


# a= [1,2,3,4]
# b=[4,3,2,1]
# print(permutation(a,b))


# rotate a matrix by 90 degrees

import numpy as np
myArr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(myArr)

def rotate(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n- layer -1
        for i in range(first,last):
            # save top
            top = matrix[layer][i]
            # left to top
            matrix[layer][i]=matrix[-i-1][layer]
            # bottom to left
            matrix[-i-1][layer]=matrix[-layer-1][-i-1]
            # move right to bottom
            matrix[-layer-1][-i-1]=matrix[i][-layer-1]
            # move to top
            matrix[i][-layer-1]=top
    return matrix


print(rotate(myArr))


