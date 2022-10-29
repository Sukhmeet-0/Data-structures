class Node:
	def __init__(self,value):
		self.value=value
		self.next=None

class Stack:
	def __init__(self,max_size):
		self.head=None
		self.tail =None
		self.max_size=max_size
	def __iter__(self):
		curNode=self.head
		while curNode:
			yield curNode
			curNode=curNode.next
	def __str__(self):
		 values=[str(x.value)for x in self]
		 return " --> ".join(values)
	def isEmpty(self):
		if self.head ==  self.tail is None:
			return True
		return False
	def isFull(self):
		if self.max_size==0:
			return True
		return False
	def push(self,value):
		newNode=Node(value)
		if self.isEmpty():
			newNode.next=self.head
			self.head=newNode
			self.tail=newNode
			self.max_size-=1
			print(f"successfully inserted {value}")

		else:
			curNode=self.head
			while curNode.next:
				curNode=curNode.next
			curNode.next=newNode
			newNode.next=None
			self.tail=newNode
			self.max_size-=1
			print(f"successfully inserted {value}")
	def peek(self):
		if self.isEmpty():
			print("Stack empty")
		else:
			print(self.tail.value)
	def pop(self):
		if self.isEmpty():
			print("Stack underflow")
		else:
			curNode=self.head
			index=0
			while curNode.next!=self.tail:
				curNode=curNode.next
			curNode.next=None
			self.tail=curNode
			self.max_size+=1
			print(f"successfully deleted {self.tail.value}")
	def deleteStack(self):
		self.head = None
		self.tail=None
		print('successfully deleted Stack')

s=Stack(4)
print(s.isEmpty())
s.peek()
s.push(0)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.isEmpty())
s.peek()
s.pop()
s.peek()
print(s)
s.deleteStack()
print(s.isEmpty())
# print([x.value for x in s])

