integers = [1, 2, 3, 4]  # ----------->O(1)
print(integers)  # ----------->O(1)
strings = ['yes', 'no', 'maybe']  # ----------->O(1)
print(strings)  # ----------->O(1)
mix = [1, 'yes', 5.6]  # ----------->O(1)
print(mix)
nested = [1, 3, 'yes', [1.2, 4.5, 3.8], 'no', 5.9]  # ----------->O(1)
print(nested)  # ----------->O(1)

# accessing

shoppingList = ['milk', 'cheese', 'butter']  # ----------->O(1)
print(shoppingList[1])  # ----------->O(1)

# traverse

for i in shoppingList:  # ----------->O(n)
    print(i, end=" ")  # ----------->O(1)
print()  # ----------->O(1)
print('bread' in shoppingList)  # ----------->O(1)
print(shoppingList[-1])  # ----------->O(1)

# update insert list

myList = [1, 2, 3, 4, 4, 5, 6, 7]  # ----------->O(1)
print(myList)  # ----------->O(1)
myList[3] = 33  # ----------->O(1)
print(myList)  # ----------->O(1)

myList.insert(0, 0)  # ----------->O(n)
print(myList)  # ----------->O(1)

myList.append(55)  # ----------->O(1)
print(myList)  # ----------->O(1)

a = [1, 1, 1, 1]  # ----------->O(1)
myList.extend(a)  # ----------->O(1)
print(myList)  # ----------->O(n)

# slicing

print(myList[2::2])
myList.pop(1)  # ----------->O(n)/1
del myList[3]  # ----------->O(n)
myList.remove(55)  # ----------->O(n)
print(myList)  # ----------->O(n)

# searching

print(7 in myList)
for i in myList:  # ----------->O(n)
    if i == 7:  # ----------->O(1)
        print(myList.index(i))  # ----------->O(1)

# concatenation of list

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a * 4)
a = a[1] * 4
print(a)
print(len(c))
print(max(c))
print(min(c))
print(sum(c))

# list from string

s = "sukhmeet-singh"
ll = list(s)
print(ll)

b = s.split("-")
print(b)

print(" ".join(s))

# pitfalls
c.append(59)
c.sort(reverse=True)
print(c)

# array vs list

import numpy as np

myArr = np.array([1, 2, 3, 4, 5])
print(myArr / 2)
