from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.isCyclicUtil(neighbor, visited, recStack):
                    return True
            elif recStack[neighbor]:
                return True 

        # This must happen AFTER checking all neighbours, outside the for loop
        recStack[v] = False
        return False

    # This method must be correctly aligned with class methods
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        
        # Changed range to start from 0 to V-1 to match your example edges
        for i in range(self.V):
            if not visited[i]:
                if self.isCyclicUtil(i, visited, recStack):
                    return True
        return False

# Driver code
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(3, 2)
g.addEdge(2, 0) 
g.addEdge(2, 3)
g.addEdge(3, 3) 
if g.isCyclic():
    print("Graph has a cycle  :)")
else:
    print("Graph has no cycle :(")
