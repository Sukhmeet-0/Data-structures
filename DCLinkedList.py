from venv import create


class Node:
	def __init__(self,value):
		self.next=None
		self.prev=None
		self.value=value

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail=None
		self.size=0
	def __iter__(self):
		temp=self.head
		while temp:
			yield temp
			temp=temp.next
	def create(self,value):
		newNode=Node(value)
		self.head=newNode
		self.tail=newNode
		newNode.next=newNode
		newNode.prev=newNode
		self.size+=1
	def insert(self,value,location):
		if self.head is None:
			create(value)

		else:
			newNode=Node(value)
			if location ==0:
				newNode.next=self.head
				newNode.prev=self.tail
				self.head.prev=newNode
				self.tail.next=newNode
				self.head=newNode
				self.size+=1
			elif location >= self.size:
				self.tail.next=newNode
				newNode.prev=self.tail
				newNode.next=self.head
				self.head.prev=newNode
				self.tail=newNode
				self.size+=1
			else:
				tempNode=self.head
				index=0
				while index<location-1:
					tempNode=tempNode.next
					index+=1
				newNode.next=tempNode.next
				newNode.prev=tempNode
				tempNode.next=newNode
				newNode.next.prev=newNode
				self.size+=1
		print("successfully inserted node")
        
	def traverse(self):
		tempNode=self.head
		while tempNode!=self.tail:
			print(tempNode.value,end=" --> ")
			tempNode=tempNode.next
		print()
	def reverseTraverse(self):
		tempNode=self.tail
		while tempNode!=self.head:
			print(tempNode.value,end=" --> ")
			tempNode=tempNode.prev



dcll = LinkedList()
dcll.create(5)
dcll.insert(0,0)
dcll.insert(5,5)
dcll.insert(3,2)
dcll.traverse()
dcll.reverseTraverse()

