a=[2,4,5,5,4,32,20,3,3,392,0,38,1,9,59,99,23]
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
            j-=1
        ls[j+1]=key
    print(ls)    


insertionSort(a)