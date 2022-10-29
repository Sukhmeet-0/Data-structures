from venv import create


class Node:
    def __init__(self,value):
        self.next=None
        self.prev=None
        self.value=value
class DLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode=tempNode.next
    def create(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        newNode.next=None
        newNode.prev=None
        self.size +=1
    def traverse(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value,end=" --> ")
            tempNode=tempNode.next
        print()
    def reverseTraverse(self):
        tempNode=self.tail
        while tempNode:
            print(tempNode.value,end=" --> ")
            tempNode=tempNode.prev
        print()
    def insert(self,value,location):
        if self.head is None:
            create(value)
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next=self.head
                newNode.prev=None
                self.head.prev=newNode
                self.head = newNode
                self.size+=1
            elif location >= self.size:
                self.tail.next=newNode
                newNode.next=None
                newNode.prev=self.tail
                self.tail = newNode
                self.size+=1
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next=newNode
                newNode.next.prev = newNode
                self.size+=1
        print("successfully inserted node")
    def delete(self,location):
        if self.head is None:
            print("No element to be deleted")
        else:
            if location==0:
                if self.head == self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=self.tail
            elif location >= self.size:
                if self.head == self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.tail = self.tail.prev
                    self.tail.next=self.head
            else:
                tempNode =self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                tempNode.next=tempNode.next.next
                tempNode.next.prev=tempNode
            print('Node successfully deleted')
    def deleteEntire(self):
        if self.head is None:
            print("Linked List does not exist")
        else:
            tempNode=self.head
            while tempNode!=self.tail:
                tempNode.prev=None
                tempNode=tempNode.next
            self.head=None
            self.tail=None
        print("successfully deleted linked list")
    def search(self,value):
        if self.head is None:
            print("There is no element to be searched")
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value == value:
                    return (f"Found {value}")
                tempNode=tempNode.next
            return ("Not found")



dll = DLinkedList()
dll.create(0)
dll.insert(1,1)
dll.insert(2,2)
dll.insert(5,20)
print(dll.search(5))
dll.delete(1)
dll.traverse()
dll.reverseTraverse()
dll.deleteEntire()
