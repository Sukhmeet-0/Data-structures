import numpy as np

# creation

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # ----------->O(1)
print(arr)  # ----------->O(1)
# print(arr.flatten())


# insertion

a = np.insert(arr, 0, [[0, 0, 0, 0]], axis=1)  # axis 0 for row | time complexity = O(row*column)
print(a)


# accessing element

def access(array, rowIndex, columnIndex):  # ----------->O(1)
    if rowIndex >= len(array) and columnIndex >= len(array):  # ----------->O(1)
        print("Incorrect Index")  # ----------->O(1)
    else:
        print(array[rowIndex][columnIndex])  # ----------->O(1)


access(arr, 1, 2)  # ----------->O(1)


def traverse(array):
    for i in range(len(arr)):  # ----------->O(n)
        for j in range(len(arr[0])): # ----------->O(n)
            print(arr[i][j], end="  ")  # ----------->O(1)
        print()  # ----------->O(1)


# ----------->O(n^2) for a square matrix
traverse(arr)


# searching

def search(array, value):  # ----------->O(1)
    for i in range(len(array)):  # ----------->O(n)
        for j in range(len(arr[0])):  # ----------->O(n)
            if array[i][j] == value:  # ----------->O(1)
                return f"value {value} found at row {i} and column {j} "  # ----------->O(1)
    return "Value not found"  # ----------->O(1)


# ----------->O(n^2) for a square matrix
print(search(arr, 10))  # ----------->O(1)


# Deletion

newArr = np.delete(arr, 0, axis=1)  # ----------->O(mn)
print(newArr)

