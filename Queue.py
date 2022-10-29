class Queue:
	def __init__(self,max_size):
		self.ls=[]
		self.max_size=max_size
		self.rear=0
		self.front=0
		# self.point=self.ls[i]
		# self.rear=self.ls[0]

	def __str__(self):
		values=[str(x) for x in self.ls]
		return " --> ".join(values)
	def isEmpty(self):
		if self.ls==[] or self.front==self.rear:
			return True
		return False
	def isFull(self):
		if len(self.ls)==self.max_size:
			return True
		return False
	def push(self,value):
		if self.isFull():
			print("Queue is Full")
		else:
			self.ls.insert(self.rear,value)
			self.rear+=1
			print(f"successfully inserted {value}")
	def pop(self):
		if self.isEmpty():
			print("Queue is already empty")
		else:
			print(f"successfully deleted value {self.ls[self.front]}")
			del self.ls[self.front]
			self.front+=1
	def peek(self):
		if self.ls==[]:
			print("There is no value present")
		else:
			print(self.ls[-1])
			
	def deleteQueue(self):
		self.ls=[]
		print("successfully deleted Queue")


q=Queue(3)
print(q.isEmpty())
print(q.isFull())
q.push(0)
print(q.isEmpty())
q.push(1)
q.push(2)
q.push(3)
print(q.isFull())
print(q)
q.pop()
print(q)
q.push(3)
print(q)
q.peek()



