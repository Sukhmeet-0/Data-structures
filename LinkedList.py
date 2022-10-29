# creation

class Node:
    def __init__(self,value):  # --------------->O(1)
        self.value=value  # --------------->O(1)
        self.next=None  # --------------->O(1)
class SLinkedList:
    def  __init__(self):  # --------------->O(1)
        self.head=None  # --------------->O(1)
        self.tail=None  # --------------->O(1)
    def __iter__(self):
        node=self.head  # --------------->O(1)
        while node:  # --------------->O(n)
            yield node  # --------------->O(1)
            node = node.next  # --------------->O(1)
    def insert(self,value,location): 
        newNode  = Node(value)  # --------------->O(1)
        if self.head is None:  # --------------->O(1)
            self.head=newNode  # --------------->O(1)
            self.tail=newNode  # --------------->O(1)
        else:
            if location == 0:  # --------------->O(1)
                newNode.next = self.head  # --------------->O(1)
                self.head = newNode  # --------------->O(1)
            elif location == -1:  # --------------->O(1)
                newNode.next = None  # --------------->O(1)
                self.tail.next = newNode  # --------------->O(1)
                self.tail=newNode  # --------------->O(1)
            else:
                tempNode=self.head  # --------------->O(1)
                index = 0  # --------------->O(1)
                while index<location-1:  # --------------->O(n)
                    tempNode=tempNode.next  # --------------->O(1)
                    index+=1  # --------------->O(1)
                nextNode = tempNode.next  # --------------->O(1)
                tempNode.next = newNode  # --------------->O(1)
                newNode.next = nextNode  # --------------->O(1)
                if tempNode == self.tail:  # --------------->O(1)
                    self.tail = newNode  # --------------->O(1)
    def traverseSLL(self): 
        if self.head is None:  # --------------->O(1) 
            print("Single LinkedList doesnot exist")  # --------------->O(1)
        else:
            node =self.head  # --------------->O(1)
            while node is not None:  # --------------->O(n)
                print(node.value,end=" --> ")  # --------------->O(1)
                node =node.next  # --------------->O(1)
        print()  # --------------->O(1)
    def search(self,value):
        if self.head is None:  # --------------->O(1)
            print("Value doesnot exist")  # --------------->O(1)
        else:
            node = self.head  # --------------->O(1)
            while node is not None:  # --------------->O(n)
                if node.value == value:  # --------------->O(1)
                    print(f"{node.value} found")  # --------------->O(1)
                    break  # --------------->O(1)
                node = node.next  # --------------->O(1)
            else:  # --------------->O(1)
                print("value does not found")  # --------------->O(1)
    def deleteNode(self,location):
        if self.head is None:  # --------------->O(1)
            print("Singly linked list doesNot exist")  # --------------->O(1)
        else:
            if location == 0:
                if self.head==self.tail:
                    self.head =None
                    self.tail=None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head==self.tail:
                    self.head =None
                    self.tail=None
                else:
                    node =self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next=None
                    self.tail=node
            else:
                tempNode = self.head
                index=0
                while index<location-1:
                    tempNode= tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next =nextNode.next
    def deleteEntire(self):
        if self.head is None:  # --------------->O(1)
            print("Linked List does not exist")  # --------------->O(1)
        else:
            self.head=None  # --------------->O(1)
            self.tail=None  # --------------->O(1)

# singleLinkedList = SLinkedList()  # --------------->O(1)
# node1 = Node(1)  # --------------->O(1)
# node2 = Node(2)  # --------------->O(1)
# singleLinkedList.head=node1  # --------------->O(1)
# singleLinkedList.head.next=node2  # --------------->O(1)
# singleLinkedList.tail=node2  # --------------->O(1) 


singlyLinkedList = SLinkedList()
singlyLinkedList.insert(1,1)
singlyLinkedList.insert(2,1)
singlyLinkedList.insert(3,1)
singlyLinkedList.insert(4,1)
singlyLinkedList.insert(0,0)
singlyLinkedList.insert(0,4)
# print([node.value for node in singlyLinkedList])
singlyLinkedList.traverseSLL()
singlyLinkedList.search(44)
singlyLinkedList.deleteNode(4)
singlyLinkedList.traverseSLL()
singlyLinkedList.deleteNode(1)
singlyLinkedList.traverseSLL()
singlyLinkedList.deleteEntire()
singlyLinkedList.traverseSLL()

