from collections import defaultdict

class Graph:
    def __init__(self,numberOfVertices):
        self.graph=defaultdict(list)
        self.numberOfVertices=numberOfVertices

    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)

    def sort(self,v,visited,stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.sort(i,visited,stack)
        
        stack.insert(0,v)

    def tsort(self):
        visit = []
        stack =[]
        for k in list(self.graph):
            if k not in visit:
                self.sort(k,visit,stack)
        print(stack)


cg=Graph(8)
cg.addEdge("A","C")
cg.addEdge("C","E")
cg.addEdge("E","H")
cg.addEdge("E","F")
cg.addEdge("F","G")
cg.addEdge("B","D")
cg.addEdge("B","C")
cg.addEdge("D","F")

cg.tsort()
