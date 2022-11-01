from queue import Queue


class Node:
    def __init__(self,value):
        self.value=value
        self.leftChild=None
        self.rightChild=None
def insertNode(rootNode,nodeValue):
    if rootNode.value==None:
            rootNode.value=nodeValue
    elif nodeValue<=rootNode.value:
        if rootNode.leftChild is None:
            rootNode.leftChild = Node(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild=Node(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue)
    print("The node has been successfully inserted")
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.value)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.value)
    preOrderTraversal(rootNode.rightChild)
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.value)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        q=Queue()
        q.put(rootNode)
        while not q.empty():
            root=q.get()
            print(root.value)
            if root.leftChild is not None:
                q.put(root.leftChild)
            if root.rightChild is not None:
                q.put(root.rightChild)

def search(rootNode,value):
    if rootNode.value==value:
        print("Found")
    elif value<rootNode.value:
        if rootNode.leftChild.value==value:
            print("found")
        else:
            search(rootNode.leftChild,value)
    else:
        if rootNode.rightChild.value==value:
            print("Found")
        else:
            search(rootNode.rightChild,value)
def minValueNode(bstNode):
    current=bstNode
    while current.leftChild is not None:
        current =current.leftChild
    return current
def deleteNode(rootNode,value):
    if rootNode is None:
        return rootNode
    if value<rootNode.value:
        rootNode.leftChild =deleteNode(rootNode.leftChild,value)
    elif value>rootNode.value:
        rootNode.rightChild=deleteNode(rootNode.rightChild,value)
    else:
        if rootNode.leftChild is None:
            temp=rootNode.rightChild
            rootNode=None
            return temp
        if rootNode.rightChild is None:
            temp=rootNode.lefttChild
            rootNode=None
            return temp
        temp=minValueNode(rootNode.rightChild)
        rootNode.value=temp.value
        rootNode.rightChild=deleteNode(rootNode.rightChild,temp.value)
    return rootNode
def deleteBST(bst):
    bst.data=None
    bst.leftChild=None
    bst.rightChild=None
    print("Successfully deleted BST")
bst = Node(None)
insertNode(bst,70)
insertNode(bst,60)
insertNode(bst,80)
insertNode(bst,90)
insertNode(bst,75)
insertNode(bst,65)
preOrderTraversal(bst)
print()
inOrderTraversal(bst)
print()
postOrderTraversal(bst)
print()
levelOrderTraversal(bst)
print()
# search(bst,655)
deleteNode(bst,70)
levelOrderTraversal(bst)
deleteBST(bst)