from array import *

a = array('i', [1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 6, 4, 3, 2, 2, 3, 2])


# def prnt(n):
#     for i in n:
#         print(i, end=" ")
#     print("\n")
#
#
# prnt(a)
#
#
# def access(arr, index):
#     if index >= len(arr):
#         print("No value present at this index")
#     else:
#         print(arr[index])
#
#
# access(a, 5)
#
#
# def app(num):
#     global a
#     a.append(n)
#     print(a)
#
#
# n = int(input("Enter the value you want to append: "))
# app(n)
#
#
# def ins(element, index):
#     global a
#     a.insert(index, element)
#     print(f"Successfully inserted {element} at index {index}")
#     print(a)
#
#
# ele = int(input("element you want to enter: "))
# ind = int(input("at which index you want to enter the value: "))
# ins(ele, ind)


def ext():
    global a
    a.extend(array('i', [55, 66, 77]))
    print(a)


ext()


def add():
    tempList = [0, 1, 2]
    global a
    a.fromlist(tempList)
    print(a)


add()


print(a.count(7))
# b = a.tostring()
b = a.tolist()
print(b)
