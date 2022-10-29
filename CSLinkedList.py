# creation

from email import header


class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class CSLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node =self.head
        while node:
            yield node
            if node.next ==self.head:
                break
            node =node.next
    def create(self,nodevalue):
        node =Node(nodevalue)
        node.next=node
        self.head = node
        self.tail=node
        print("The Linked list has been created")
    def insert(self,value,location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail=newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head  = newNode
                self.tail.next = self.head
            elif location == -1:
                newNode.next=self.tail.next
                self.tail.next = newNode
                self.tail= newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
            print(f"{value} successfully inserted")
    def traverse(self):
        if self.head is None:
            print("Linked List doesnot exist")
        else:
            node  = self.head
            while node:
                print(node.value,end=" --> ")
                node =node.next
                if node == self.tail:
                    break

        print()
    def search(self,value):
        if self.head is None:
            print("value doesnot exist")
        else:
            node = self.head
            while node:
                if node.value == value:
                    print(f"{value} found ")
                    break
                node = node.next
            else:
                print("Not found")
    def delete(self,location):
        if self.head == None:
            print("Cannot delete as linked list doesnot exist")
        else:
            if location ==0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node =self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=self.head
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index<location -1:
                    tempNode=tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next




    def deleteEntire(self):
        if self.head is None:
            print("Linked list not present")
        else:
            self.head =None
            self.tail=None
            print('successfully deleted linked list')




csl = CSLinkedList()
csl.insert(0,0)
csl.insert(1,1)
csl.insert(2,2)
csl.insert(3,3)
csl.insert(4,4)
csl.insert(5,5)
csl.insert(6,6)
# print([node.value for node in csl])
csl.traverse()
csl.search(5)
csl.delete(4)
csl.traverse()
csl.deleteEntire()
csl.traverse()

