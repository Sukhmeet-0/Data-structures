class Heap:
    def __init__(self,size):
        self.size=size
        self.ls=(size+1)*[None]
        self.heapsize=0
        self.maxsize=size+1

def peekOfHeap(root):
    if not root:
        return
    else:
        return root.ls[1]

def sizeOfHeap(root):
    if not root:
        return 
    else:
        return root.heapsize
def levelOrder(root):
    if not root:
        return 
    else:
        for i in range(1,root.heapsize+1):
            print(root.ls[i])
def heapify(root,index,heapType):
    parentIndex=int(index/2)
    if index<=1:
        return
    if heapType=="Min":
        if root.ls[index]<root.ls[parentIndex]:
            temp=root.ls[index]
            root.ls[index]=root.ls[parentIndex]
            root.ls[parentIndex]=temp
        heapify(root,parentIndex,heapType)
    if heapType=="Max":
        if root.ls[index]>root.ls[parentIndex]:
            temp=root.ls[index]
            root.ls[index]=root.ls[parentIndex]
            root.ls[parentIndex]=temp
        heapify(root,parentIndex,heapType) 
def insert(root,value,heapType):
    if root.heapsize+1==root.maxsize:
        return "Heap is full"
    root.ls[root.heapsize+1]=value
    root.heapsize+=1
    heapify(root,root.heapsize,heapType)
    return "Value has been successfully inserted"
def extract(root,index,heapType):
    leftIndex=index*2
    rightIndex=index*2+1
    swapChild=0
    if root.heapsize<leftIndex:
        return
    elif root.heapsize==leftIndex:
        if heapType=="Min":
            if root.ls[index]>root.ls[leftIndex]:
                temp=root.ls[index]
                root.ls[index]=root.ls[leftIndex]
                root.ls[leftIndex]=temp
            return
        else:
            if root.ls[index]<root.ls[leftIndex]:
                temp=root.ls[index]
                root.ls[index]=root.ls[leftIndex]
                root.ls[leftIndex]=temp
            return
    else:
        if heapType=="Min":
            if root.ls[leftIndex]<root.ls[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if  root.ls[index]>root.ls[swapChild]:
                temp=root.ls[index]
                root.ls[index]=root.ls[swapChild]
                root.ls[swapChild]=temp
        else:
            if root.ls[leftIndex]>root.ls[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if  root.ls[index]<root.ls[swapChild]:
                temp=root.ls[index]
                root.ls[index]=root.ls[swapChild]
                root.ls[swapChild]=temp  
        heapify(root,swapChild,heapType) 
def extractNode(root,heapType):
    if root.heapsize==0:
        return 
    else:
        extractNoded=root.ls[1]
        root.ls[1]=root.ls[root.heapsize]
        root.ls[root.heapsize]=None
        root.heapsize-=1
        extract(root,1,heapType)
        return extractNode
def deleteHeap(root):
    if root.heapsize==0:
        print("heap not found")
    else:
        root.ls=None
        print("successfully deleted heap")
nbh=Heap(5)
print(sizeOfHeap(nbh))
insert(nbh,5,"Max")
insert(nbh,4,"Max")
insert(nbh,3,"Max")
insert(nbh,2,"Max")
insert(nbh,1,"Max")
levelOrder(nbh)
extractNode(nbh,"Max")
print()
levelOrder(nbh)
deleteHeap(nbh)