class BinaryTree:
	def __init__(self,size):
		self.List=size*[None]
		self.lastUsedIndex=0
		self.max_size=size
	def insertNode(self,value):
		if self.lastUsedIndex+1==self.max_size:
			return "The binary tree is full"
		else:
			self.List[self.lastUsedIndex+1]=value
			# print(self.List[self.lastUsedIndex+1])
			self.lastUsedIndex+=1
			return"The value has been successfully inserted"
	def search(self,value):
		for i in self.List:
			if i == value:
				return("Found")
		return "Not Found"
	def preOrderTraversal(self,index=1):
		if index>self.lastUsedIndex:
			return 
		print(self.List[index])
		self.preOrderTraversal(index*2)
		self.preOrderTraversal(index*2+1)
	def inOrderTraversal(self,index=1):
		if index > self.lastUsedIndex:
			return
		self.inOrderTraversal(index*2)
		print(self.List[index])
		self.inOrderTraversal(index*2+1)
	def postOrderTraversal(self,index=1):
		if index > self.lastUsedIndex:
			return
		self.postOrderTraversal(index*2)
		self.postOrderTraversal(index*2+1)
		print(self.List[index])
	def levelOrderTraversal(self,index=1):
		if index>self.lastUsedIndex:
			return
		for i in range(index,self.lastUsedIndex+1):
			print(self.List[i])
	def deleteNode(self,value):
		if self.lastUsedIndex==0:
			print("Tree doesnot exist")
		else:
			for i in range(1,self.lastUsedIndex+1):
				if self.List[i]==value:
					self.List[i]=self.List[self.lastUsedIndex]
					self.List[self.lastUsedIndex]=None
					self.lastUsedIndex-=1
					print(f"Deleted node {value}")
	def deleteTree(self):
		self.List=None
		print("Successfully deleted Binary Tree")

newBt=BinaryTree(8)
print(newBt.insertNode("Drinks"))
print(newBt.insertNode("Hot"))
print(newBt.insertNode("Cold"))
print(newBt.search("Hot"))
newBt.preOrderTraversal()
print()
newBt.inOrderTraversal()
print()
newBt.postOrderTraversal()
print()
newBt.levelOrderTraversal()
print()
newBt.deleteNode("Hot")
print()
newBt.levelOrderTraversal()
print()
newBt.deleteTree()
