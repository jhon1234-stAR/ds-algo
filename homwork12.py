def is_graph_connected(graph):
  
    if not graph:
        return True
        
   
    visited = set()
    
 
    all_nodes = list(graph.keys())
    
    def dfs(node):
        visited.add(node)
  
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
                

    start_node = all_nodes[0]
    dfs(start_node)
    

    return len(visited) == len(graph)

graph_strings = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}
print(is_graph_connected(graph_strings))  
# Output: True

# Example 2: Disconnected graph with skipped integer IDs (Fixed brackets here)
graph_numbers = {
    10: [],
    20: [],
    99: []
}
print(is_graph_connected(graph_numbers))
# Output: False




