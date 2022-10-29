class Stack:
	def __init__(self,max_size):
		self.max_size=max_size
		self.ls=[]
	def __str__(self):
		values=self.ls.reverse()
		values=[str(x) for x in self.ls]
		return "\n".join(values)
	def isEmpty(self):
		if self.ls==[]:
			return True
		return False
	def isFull(self):
		if len(self.ls)==self.max_size:
			return True
		return False
	def push(self,value):
		if self.isFull():
			print("Stack overflow")
		else:
			self.ls.append(value)
			print(f"successfully inserted value {value}")
	def pop(self):
		if self.isEmpty():
			print("Stack underflow")
		else:
			self.ls.pop()
	def peek(self):
		if self.isEmpty():
			print("Stack is empty")
		else:
			print(self.ls[-1])
	def deleteStack(self):
		self.ls=[]
		print('successfully deleted Stack')


s=Stack(5)
print(s.isEmpty())
s.push(0)
s.push(1)
s.push(2)
s.push(3)
print(s.isFull())
s.push(4)
print(s.isFull())
s.peek()
s.pop()
s.peek()
print(s)
s.deleteStack()
print(s.isEmpty())