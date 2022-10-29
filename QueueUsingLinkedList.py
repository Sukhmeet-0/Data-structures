


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Q:
    def __init__(self):
        self.head=None
        self.tail=None
        self.head=self.tail
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def isEmpty(self):
        if self.head==None:
            return True
        return False
    def pop(self):
        if self.isEmpty():
            print("No element present to be deleted")
        else:
            print(f"successfully deleted {self.head.value}")
            self.head=self.head.next
    def push(self,value):
        node=Node(value)
        if self.isEmpty():
            node.next=None
            self.head=node
            self.tail=node
            print(f"successfully inserted {value} ")
        else:
            self.tail.next=node
            self.tail=node
            self.tail.next=None
            print(f"successfully inserted {value} ")
    def peek(self):
        if self.isEmpty():
            print("No element present")
        else:
            print(self.tail.value)
    def deleteQ(self):
        if self.isEmpty():
            print('Queue not present')
        else:
            self.head=None
            self.tail=None
            print("Deleted Queue successfully")


s= Q()
print(s.isEmpty())
s.peek()
s.pop()
s.push(0)
s.peek()
s.push(1)
s.peek()
s.push(2)
s.peek()
s.push(3)
s.peek()
s.push(4)
s.peek()
s.pop()
s.pop()
s.pop()
s.pop()
s.deleteQ()
s.pop()
s.pop()


print([(x.value) for x in s])