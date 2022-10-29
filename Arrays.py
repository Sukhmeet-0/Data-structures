from array import *

# creation

arrayName = array('i', [1, 2, 3, 4, 5])  # ------------->O(n)


# print(arrayName)
#
# arr2 = array('d', [1.3, 4.3, 2.4, 5.3])
# print(arr2)  # ------------------>O(1)
#
# # insertion
#
# arrayName.insert(5, 7)  # ------------->O(1)
# print(arrayName)
#
# arrayName.insert(0, 0)  # ------------->O(n)
# print(arrayName)
#
# # traversal
#
# for i in arrayName:  # ------------->O(n)
#     print(i, end=" ")  # ------------->O(1)
#     # print("\n")


# accessing element

def access(index, arr):  # ------------->O(1)
    if index >= len(arr):  # ------------->O(1)
        print("There is no element present at this index")  # ------------->O(1)
    else:
        print(arr[index])  # ------------->O(1)


access(4, arrayName)  # ------------->O(1)


# search element

def search(n, arr):  # ------------->O(1)
    for i in arr:  # ------------->O(n)
        if i == n:  # ------------->O(1)
            print(f"Found {i} at index {arr.index(n)}")  # ------------->O(1)
            break  # ------------->O(1)
        else:
            continue  # ------------->O(1)
        print("element not found")  # ------------->O(1)


search(4, arrayName)


# deleting element

n = int(input("Enter element which you want to delete: "))  # ------------->O(1)
arrayName.remove(n)  # ------------->O(n) because we have to rearrange elements after removal of an element from array
print(f"{n} removes successfully from array")  # ------------->O(1)
print(arrayName)  # ------------->O(1)

