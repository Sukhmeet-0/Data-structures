from queue import Queue
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=1

def preOrderTraversal(root):
    if not root:
        return
    else:
        print(root.value)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)
def inOrderTraversal(root):
    if not root:
        return
    else:
        inOrderTraversal(root.left)
        print(root.value)
        inOrderTraversal(root.right)
def postOrderTraversal(root):
    if not root:
        return
    else:
        postOrderTraversal(root.left)
        print(root.value)
        postOrderTraversal(root.right)
def levelOrderTraversal(root):
    if not root:
        return
    else:
        q=Queue()
        q.put(root)
        while not q.empty():
            rs=q.get()
            print(rs.value)
            if rs.left is not None:
                q.put(rs.left)
            if rs.right is not None:
                q.put(rs.right)
def search(root,value):
    if not root:
        print("Tree not exist")
    elif value<root.value:
        if root.left.value==value:
            print("Found")
        else:
            search(root.left,value)
    else:
        if root.right.value==value:
            print("found")
        else:
            search(root.right,value)
def getHeight(root):
    if not root:
        return 0
    return root.height
# def rightRotate(disbalancedNode):
#     newRoot=disbalancedNode.left
#     disbalancedNode.left=disbalancedNode.left.right
#     disbalancedNode.left.right=newRoot
#     newRoot.left=disbalancedNode.left
#     disbalancedNode.height=1+max(getHeight(disbalancedNode.left),getHeight(disbalancedNode.right))
#     newRoot.height=1+max(getHeight(newRoot.left),getHeight(newRoot.right))
#     return newRoot
def rightRotate( z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(getHeight(z.left),
                        getHeight(z.right))
        y.height = 1 + max(getHeight(y.left),
                        getHeight(y.right))
 
        # Return the new root
        return y
# def leftRotate(dbn):
#     nr=dbn.right
#     dbn.right=dbn.right.left
#     dbn.right=dbn
#     dbn.right=dbn.right.left
#     dbn.height==1+max(getHeight(dbn.left),getHeight(dbn.right))
#     nr.height=1+max(getHeight(nr.left),getHeight(nr.right))
#     return nr
def leftRotate( z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(getHeight(z.left),
                        getHeight(z.right))
        y.height = 1 + max(getHeight(y.left),
                        getHeight(y.right))
 
        # Return the new root
        return y
def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)
# def insert(root,value):
#     if not root:
#         return Node(value)
#     elif value<root.value:
#         root.left=insert(root.left,value)
#     elif value>root.value:
#         root.right=insert(root.right,value)
#     root.height=1+max(getHeight(root.left),getHeight(root.right))
#     balance=getBalance(root)
#     if balance>1 and value<root.left.value:
#         return rightRotate(root)
#     if balance>1 and value>root.left.value:
#         root.left=leftRotate(root.left)
#         return rightRotate(root)
#     if balance<-1 and value>root.right.value:
#         return leftRotate(root)
#     if balance<-1 and value<root.right.value:
#         root.right=rightRotate(root.right)
#         return leftRotate(root)
#     return root
def insert( root, key):
     
        # Step 1 - Perform normal BST
        if not root:
            return Node(key)
        elif key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(getHeight(root.left),
                           getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = getBalance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.value:
            return rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and key > root.right.value:
            return leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and key > root.left.value:
            root.left = leftRotate(root.left)
            return rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and key < root.right.value:
            root.right = rightRotate(root.right)
            return leftRotate(root)
 
        return root
def getMinValueNode(root):
    if root is None or root.left is None:
        return root
    return getMinValueNode(root.left)
def deleteNode(root,value):
    if not root:
        return root
    elif value<root.value:
        root.left=deleteNode(root.left,value)
    elif value>root.value:
        root.right=deleteNode(root.right,value)
    else:
        if root.left is not None:
            temp=root.right
            root=None
            return temp
        elif root.right is not None:
            temp=root.right
            root=None
            return temp
        temp=getMinValueNode(root.right)
        root.value=temp.value
        root.right=deleteNode(root.left,temp.value)
    balance=getBalance(root)
    if balance>1 and getBalance(root.left)>=0:
        return rightRotate(root)
    if balance<-1 and getBalance(root.right)<=0:
        return leftRotate(root)
    if balance>1 and getBalance(root.left)<0:
        root.left=leftRotate(root.left)
        return rightRotate(root)
    if balance<-1 and getBalance(root.right)>0:
        root.right=rightRotate(root.right)
        return leftRotate(root)
    return root
def deleteTree(root):
    root.value=None
    root.left=None
    root.right=None
    print("Tree deleted successfully")
t=Node(5)
insert(t,10)
insert(t,15)
insert(t,20)
insert(t,25)
# search(t,20)
preOrderTraversal(t)
levelOrderTraversal(t)
deleteTree(t)
