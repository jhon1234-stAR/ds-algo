class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, v, temp, visited):
        visited[v] = True

        temp.append(v)
        for i in self.adj[v]:
            if not visited[i]:
                self.DFSUtil(i, temp, visited)
        return temp



    def addEdge(self, v , w):
        self.adj[v].append(w)
        self.adj[w].append(v)


    def connectedComponents(self):
        visited = []
        cc = []

        for i in range(self.V):
            visited.append(False)
        for i in range(self.V):
            if not visited[i]:
                temp = []
                cc.append(self.DFSUtil(i, temp, visited))
        return cc



if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(2,3)
    g.addEdge(8,4)
    print(g)
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)