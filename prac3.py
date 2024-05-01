class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, w):
        if u in self.graph:
            self.graph[u].append((v, w))
        else:
            self.graph[u] = [(v, w)]
        
        if v in self.graph:
            self.graph[v].append((u, w))
        else:
            self.graph[v] = [(u, w)]
    
    def prim_mst(self):
        mst = []
        visited = set()
        start = next(iter(self.graph))  # Start from any vertex
        
        visited.add(start)
        
        while len(visited) < len(self.graph):
            min_edge = None
            min_weight = float('inf')
            
            for vertex in visited:
                for neighbor, weight in self.graph[vertex]:
                    if neighbor not in visited and weight < min_weight:
                        min_weight = weight
                        min_edge = (vertex, neighbor, weight)
            
            if min_edge:
                mst.append(min_edge)
                visited.add(min_edge[1])
        
        return mst

# Example usage:
g = Graph()
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 1)
g.add_edge('C', 'D', 2)

mst = g.prim_mst()
print("Prim's Minimum Spanning Tree:")
for edge in mst:
    print(edge)
