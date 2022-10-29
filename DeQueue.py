class Dq:
	def __init__(self,size):
		self.size=size
		self.q=[]
		self.rear=0
		self.front=0
	def __str__(self):
		values=[str(x) for x in self.q]
		return " --> ".join(values)
	def isEmpty(self):
		if self.q==[]:
			# self.front=0
			return True
		return False
	def pop(self):
		if self.isEmpty():
			print('Queue already empty')
		else:
			print(f"successfully deleted {self.q[self.front]} from location {self.front}")
			del self.q[self.front]
			self.front+=1
			if self.front==self.size:
				self.front=0
	def isFull(self):
		if len(self.q)==self.size:
			# self.rear=0
			return True
		return False
	def push(self,value):
		if self.isFull() :
			print("Delete an element first")
		else:
			print(f"successfully inserted {value} at location {self.rear}")
			self.q.insert(self.rear,value)
			self.rear+=1
			if self.rear == self.size:
				self.rear=0
	def peek(self):
		if self.isEmpty():
			print("No element present")
		else:
			if self.rear==0:
				print(self.q[-1])
			else:
				print(self.q[self.rear-1])
	def delete(self):
		if self.ls==[]:
			print("queue no present")
		else:
			self.q.clear()
			print("successfully deleted Queue")


d=Dq(3)
print(d.isEmpty())
print(d.isFull())
d.push(0)
d.push(1)
d.push(2)
d.peek()
print(d)
print(d.isFull())
d.push(2)
d.pop()
print(d)
d.push(3)
print(d)
d.peek()
d.push(4)
d.pop()
d.peek()
d.push(4)
print(d)
d.peek()





