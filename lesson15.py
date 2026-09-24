class Graph:
    def __init__(self):
        self.adj_list={}


    def add_edge(self,u,v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v]=[]


            self.adj_list[u].append(v)
            self.adj_list[v].append(u)



    def dfs(self,start,target,visited):
        if start==target:
            return True

        
        visited.add(start)

        for neighbor in self.adj_list[start]:
            if neighbor not in visited:
                if self.dfs(neighbor, target, visited):
                    return True
                
        return False

    def if_path_exists(self,start,target):
        visited=set()
        return self.dfs(start,target,visited)

graph = Graph()
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,3)
graph.add_edge(2,3)
graph.add_edge(3,5)

start_node = 0
target_node = 4

if graph.if_path_exists(start_node,target_node):
    print(f"a path exist between {start_node} and {target_node}")
else:
    print("nope nothing for your eyes to see here")

