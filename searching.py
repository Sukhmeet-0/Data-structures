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
    start=0
    end=len(a)-1
    m=math.floor((start+end)/2)
    # print(start,m,end)
    while not a[m]==v:
        if v<a[m]:
            end=m-1
        else:
            start=m+1
        m=math.floor((start+end)/2)
        # print(start,m,end)
    if a[m]==v:
        return (f"found {a[m]} at location {m}")
    else:
        return ("Not found")

print(a)
print(binarySearch(a,9))