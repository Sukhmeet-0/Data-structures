class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)
    
    def BFS(self,vertex):
        visited =[vertex]
        queue=[vertex]
        while queue:
            deVertex=queue.pop(0)
            print(deVertex, end=" ")
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex) # ------------O(V+E)

    def DFS(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            deVertex=stack.pop()
            print(deVertex,end=" ")
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)  # ---------------o(V+E)


cd= {"a":["b","c"],
     "b":["a","d","e"],
     "c":["a","e"],
     "d":["b","e","f"],
     "e":["d","f"],
     "f":["d","e"]}

graph=Graph(cd)
# graph.addEdge("e","c")
graph.BFS("a")
print()
graph.DFS("a")
# print(graph.gdict)







# class Graph:
#     def __init__(self):
#         self.adjacent_list={}
#     def addVertex(self,vertex):
#         if vertex not in self.adjacent_list.keys():
#             self.adjacent_list[vertex]=[]
#             return True
#         return False
#     def print_graph(self):
#         for vertex in self.adjacent_list:
#             print(vertex,":",self.adjacent_list[vertex])
#     def addEdge(self,vertex,edge):
#         if vertex in self.adjacent_list.keys() and edge in self.adjacent_list.keys():
#             self.adjacent_list[vertex].append(edge)
#             self.adjacent_list[edge].append(vertex)
#             return True
#         return False
#     def removeEdge(self,vertex,edge):
#         if vertex in self.adjacent_list.keys() and edge in self.adjacent_list.keys():
#             try:
#                 self.adjacent_list[vertex].remove(edge)
#                 self.adjacent_list[edge].remove(vertex)
#             except ValueError:
#                 pass
#     def removeVertex(self,vertex):
#         if vertex in self.adjacent_list.keys():
#             try:
#                 for other_vertex in self.adjacent_list[vertex]:
#                     self.adjacent_list[other_vertex].remove(vertex)
#                 del self.adjacent_list[vertex]
#                 return True
#             except ValueError:
#                 pass
#             return False
#     def BFS(self,vertex):
#         visited =[vertex]
#         queue=[vertex]
#         while queue:
#             deVertex=queue.pop(0)
#             print(deVertex)
#             for adjacentVertex in self.adjacent_list[vertex]:
#                 if adjacentVertex not in visited:
#                     visited.append(adjacentVertex)
#                     queue.append(adjacentVertex)

# g=Graph()
# # g.addVertex("A")
# # g.addVertex("B")
# # g.addEdge("A","B")
# # g.removeEdge("A","B")
# # g.removeVertex("A")
# # g.print_graph()