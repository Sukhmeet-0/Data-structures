
from LLE import LinkedList,Node

# remove duplicates from linked list

# def removeDups(ll):
#     if ll.head is None:
#         return 
#     else:
#         tempNode=ll.head
#         visited = set([tempNode.value])
#         while tempNode.next:
#             if tempNode.next.value in visited:
#                 tempNode.next=tempNode.next.next
#             else:
#                 visited.add(tempNode.next.next)
#                 tempNode=tempNode.next
#         return ll
# def removeDups1(ll):
#     if ll.head is None:
#         return
#     tempNode = ll.head
#     while tempNode:
#         runner = tempNode
#         while runner.next:
#             if runner.next.value==tempNode.value:
#                 runner.next=runner.next.next
#             else:
#                 runner=runner.next
#         tempNode=tempNode.next
#     return ll.head

# customLL =LinkedList()
# customLL.generate(10,0,99)
# print(customLL)
# removeDups1(customLL)
# print(customLL)


# return kth element to last

# def returnKthElement(ll,k):
#     if k == 0:
#         faulty=ll.head
#         ll.head=ll.head.next
#         ll.head.prev=None
#         ll.tail.next=faulty
#         faulty.prev=ll.tail
#         ll.tail=faulty
#         faulty.next=None
#     else:
#         tempNode=ll.head
#         index=0
#         while index<k-1:
#             tempNode=tempNode.next
#             index+=1
#         faulty=tempNode.next
#         tempNode.next=tempNode.next.next
#         tempNode.next.prev=tempNode
#         ll.tail.next=faulty
#         faulty.next=None
#         faulty.prev=ll.tail
#         ll.tail=faulty

# customLL = LinkedList()
# customLL.generate(10,0,99)
# print(customLL)
# returnKthElement(customLL,1)
# print(customLL)


# partition of linked list

def partition(ll,x):
    curNode=ll.head
    ll.tail=ll.head

    while curNode:
        nextNode=curNode.next
        curNode.next=None
        if curNode.value < x:
            curNode.next=ll.head
            ll.head=curNode
        else:
            ll.tail.next=curNode
            ll.tail=curNode
        curNode=nextNode

    if ll.tail.next is not None:
        ll.tail.next=None
    
l =LinkedList()
l.generate(10,0,99)
print(l)
partition(l,30)
print(l)







# sumList(llA,llB):
# def sumList(llA,llB):
#     n1=llA.head
#     n2=llB.head
#     carry=0
#     ll=LinkedList()

#     while n1 or n2:
#         result = carry
#         if n1:
#             result+=n1.value
#             n1=n1.next
#         if n2:
#             result+=n2.value
#             n2=n2.next
#         ll.add(int(result%10))
#         carry=result/10
#     return ll

    
# llA=LinkedList()
# llA.add(7)
# llA.add(1)
# llA.add(6)


# llB = LinkedList()
# llB.add(5)
# llB.add(9)
# llB.add(2)

# print(llA)
# print(llB)
    
# print(sumList(llA,llB))


# intersection Linked List

def intersection(a,b):
    if a.tail is not b.tail:
        return False
    lenA=len(a)
    lenB=len(b)
    shorter = a if lenA<lenB else b
    longer = b if lenA<lenB else a
    diff = len(longer)-len(shorter)

    longerNode=longer.head
    shorterNode=shorter.head
    for i in range(diff):
        longerNode=longerNode.next
    while shorterNode is not longerNode:
        shorterNode=shorterNode.next
        longerNode=longerNode.next
    return longerNode


# helper addition

def addSameNode(a,b,value):
    tempNode=Node(value)
    a.tail.next=tempNode
    a.tail=tempNode
    b.tail.next=tempNode
    b.tail=tempNode


a =LinkedList()
a.generate(3,0,10)
b=LinkedList()
b.generate(4,0,10)

addSameNode(a,b,11)
addSameNode(a,b,13)

print(a)
print(b)
print(intersection(a,b))
# ---------------------------------------------->O(A+B)
