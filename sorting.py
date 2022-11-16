a=[2,4,5,5,4,32,20,3,3,392,38,1,9,59,99,23]
def bubbleSort(ls):
    for i in range(len(ls)-1):
        for j in range(len(ls)-i-1):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
    print(ls)

bubbleSort(a)


def selectionSort(ls):
    for i in range(len(ls)):
        min=i
        for j in range(i+1,len(ls)):
            if ls[min]>ls[j]:
                min=j
        ls[i],ls[min]=ls[min],ls[i]
    print(ls)

selectionSort(a)   

def insertionSort(ls):
    for i in range(1,len(ls)):
        key=ls[i]
        j=i-1
        while j>=0 and key<ls[j]:
            ls[j+1]=ls[j]
        ls[j+1]=key
    # print(ls) 
    return ls  


print(insertionSort(a))
import math
def bucketSort(ls):
    numberOfBuckets=round(math.sqrt(len(ls)))
    maxx=max(ls)
    arr=[]
    for i in range(numberOfBuckets):
        arr.append([])
    for j in ls:
        index=math.ceil(j*numberOfBuckets/maxx)
        arr[index-1].append(j)
    for i in range(numberOfBuckets):
        arr[i]=insertionSort(arr[i])
    k=0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            ls[k]=arr[i][j]
            k+=1
    return ls #--------------O(n^2)

print(bucketSort(a))
def merge(ls,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(0,n1):
        L[i]=ls[l+i]
    for j in range(0,n2):
        R[j]=ls[m+1+j]
    i=0
    j=0
    k=l
    while i <n1 and j<n2:
        if L[i]<=R[j]:
            ls[k]=L[i]
            i+=1
        else:
            ls[k]=R[j] 
            j+=1
        k+=1
    while i <n1:
        ls[k]=L[i]
        i+=1
        k+=1
    while j <n2:
        ls[k]=R[j]
        j+=1
        k+=1
def mergeSort(ls,l,r):
    if l<r:
        m=(l+r-1)//2
        mergeSort(ls,l,m)
        mergeSort(ls,m+1,r)
        merge(ls,l,m,r)
    return ls
print(mergeSort(a,0,15)) #--------------O(nlogn)

def partition(ls,low,high):
    i=low-1
    pivot=ls[high]
    for j in range(low,high):
        if ls[j]<=pivot:
            i+=1
            ls[i],ls[j]=ls[j],ls[i]
    ls[i+1],ls[high]=ls[high],ls[i+1]
    return i+1
def quickSort(ls,low ,high):
    if low<high:
        pi=partition(ls,low,high)
        quickSort(ls,low,pi-1)
        quickSort(ls,pi+1,high)
    return ls #------------o(nlogn)

print(quickSort(a,0,15))
def heapify(ls,n,i):
    smallest=i
    l = 2*i+1
    r=2*i+2
    if l< n and ls[l]<ls[smallest]:
        smallest=l
    if r < n and ls[r]<ls[smallest]:
        smallest = r
    if smallest !=i:
        ls[i],ls[smallest]=ls[smallest],ls[i]
        heapify(ls,n,smallest)       
def heapSort(ls):
    n =len(ls)
    for i in range(int(n/2)-1,-1,-1):
        heapify(ls,n,i)
    for i in range(n-1,0,-1):
        ls[i],ls[0]=ls[0],ls[i]
        heapify(ls,i,0)
    ls.reverse() # -----------o(nlogn)
    return ls
print(heapSort(a))