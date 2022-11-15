class Node:
    def __init__(self):
        self.children={}
        self.endOfStringa=False

class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,word):
        current=self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node==None:
                node=Node()
                current.children.update({ch:node})
            current=node
        current.endOfStringa=True
        print("Sucessfully inserted")
    def search(self,word):
        currentNode=self.root
        for i in word:
            node=currentNode.children.get(i)
            if node==None:
                return False
            currentNode=node
        if currentNode.endOfStringa==True:
            return True
        else:
            return False
def deleteString(root,word,index):
    ch =word[index]
    currentNode=root.children.get(ch)
    canThisBeDeleted=False

    if len(currentNode.children)>1:
        deleteString(currentNode,word,index+1)
        return False
    if index==len(word)-1:
        if len(currentNode.children)>=1:
            currentNode.endOfString=False
            return False
        else:
            root.children.pop(ch)
            return True
    if currentNode.endOfStringa==True:
        deleteString(currentNode,word,index+1)
        return False
    canThisBeDeleted=deleteString(currentNode,word,index+1)
    if canThisBeDeleted==True:
        root.children.pop(ch)
        return True
    else:
        return False

nt=Trie()
nt.insert("App")
nt.insert("Appl")
print(nt.search("App"))
deleteString(nt.root,"App",0)
print(nt.search("App"))