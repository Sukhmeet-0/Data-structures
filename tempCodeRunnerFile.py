# linear search
a=[2,4,5,5,4,32,20,3,3,392,38,1,9,59,99,23]
for i in a:
    if i==9:
        print(f"Found {i}")
        break
else:
    print("Not Found")

# binary search
import math
a.sort()
def binarySearch(a,v):