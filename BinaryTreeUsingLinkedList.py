from queue import Queue

from numpy import equal
class TreeNode:
	def __init__(self,data):
		self.data=data
		self.leftChild=None
		self.rightChild=None

newBt=TreeNode("Drinks") # -------------->O(1)
hot=TreeNode("Hot")
cold=TreeNode("Cold")
newBt.leftChild=hot
newBt.rightChild=cold
tea=TreeNode("Tea")
coffee=TreeNode('Coffee')
hot.leftChild=tea
hot.rightChild=coffee
cola=TreeNode('Cola')
fanta=TreeNode("Fanta")
cold.leftChild=cola
cold.rightChild=fanta


def preOrderTraversal(rootNode):
	if not rootNode:  # -------------->O(1)
		return
	print(rootNode.data)  # -------------->O(1)
	preOrderTraversal(rootNode.leftChild)  # -------------->O(n/2)
	preOrderTraversal(rootNode.rightChild)  # -------------->O(n/2)

preOrderTraversal(newBt)
print()

def inOrderTraversal(rootNode):
	if not rootNode:
		return
	inOrderTraversal(rootNode.leftChild)  # -------------->O(n/2)
	print(rootNode.data)
	inOrderTraversal(rootNode.rightChild)  # -------------->O(n/2)

inOrderTraversal(newBt)
print()


def postOrderTraversal(rootNode):
	if not rootNode:
		return
	postOrderTraversal(rootNode.leftChild)  # -------------->O(n/2)
	postOrderTraversal(rootNode.rightChild)  # -------------->O(n/2)
	print(rootNode.data)


postOrderTraversal(newBt)
print()

def levelOrderTraversal(rootNode):
	if not rootNode:
		return
	else:
		Q=Queue()
		Q.put(rootNode)
		while not (Q.empty()):
			node=Q.get()
			if node==None:
				continue
			print(node.data)
			Q.put(node.leftChild)
			Q.put(node.rightChild)

levelOrderTraversal(newBt)
print()


def search(root,value):
	if root is None:
		print("Tree doesnot exist")
	else:
		q=Queue()
		q.put(root)
		while not(q.empty()):
			rs=q.get()
			if  value == rs.data:
				print(f"Successfully found {value}")
				break
			if rs.leftChild is not None:
				q.put(rs.leftChild)
			if rs.rightChild is not None:
				q.put(rs.rightChild)
		else:
			print(f"{value} Not found")


search(newBt,'Fanta')
		

