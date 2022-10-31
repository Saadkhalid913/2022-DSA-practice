from __future__ import annotations
from typing import List, Tuple, Type, Union, Any

class Queue():
    def __init__(self, items: List[Any] = []):
        self.items = items 

    def add(self, item):
        self.items.append(item)

    def remove(self):
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)
    def __contains__(self, x):
        return x in self.items

'''

My Graph Theory Practice File 

'''



# Undirected Graph Implementation

class UndirectedUnweightedGraph():

    def __init__(self, n: int):
        self.n: int = n 
        self.adj_matrix: List[List[int]] = []

        for i in range(n):
            self.adj_matrix.append([False for j in range(self.n) ])
        
        for i in range(n):
            self.adj_matrix[i][i] = True

    def __repr__(self) -> str:
        return "\n".join(map(str, self.adj_matrix))

    def add(self, a, b):
        assert a < self.n and b < self.n 

        self.adj_matrix[a][b] = True
        self.adj_matrix[b][a] = True

    def remove(self, a, b):
        assert a < self.n and b < self.n 

        self.adj_matrix[a][b] = False
        self.adj_matrix[b][a] = False
    

## Undirected Weighted Graph 
class UndirectedWeightedGraph():
    def __init__(self, n: int):
            self.n: int = n 
            self.adj_matrix: List[List[int]] = []

            for i in range(n):
                self.adj_matrix.append([float("inf") for j in range(self.n) ])
            
            for i in range(n):
                self.adj_matrix[i][i] = 0

    def __repr__(self) -> str:
        return "\n".join(map(str, self.adj_matrix))

    def add(self, a, b, w):
        assert a < self.n and b < self.n 

        self.adj_matrix[a][b] = w
        self.adj_matrix[b][a] = w

    def remove(self, a, b):
        assert a < self.n and b < self.n 

        self.adj_matrix[a][b] = float("inf")
        self.adj_matrix[b][a] = float("inf")

    def ShortestPath(self, a, b):

        distances = [float("inf") for i in range(self.n)]
        distances[a] = 0

        visited = [False for i in range(self.n)]
        nodes: List[Tuple[int, int]] = []
        nodes.append((a, 0))

        while len(nodes) > 0: # worst case (we need to try every node is O(n))
            cur_node_tuple = nodes.pop(0)
            cur_node = cur_node_tuple[0]

            visited[cur_node] = True 

            neighbors = self.adj_matrix[cur_node]

            for neighbor, distance in enumerate(neighbors): # worst case O(n)
                if visited[neighbor]:
                    continue 

                if distances[neighbor] > distance + distances[cur_node]:
                    distances[neighbor] = distance + distances[cur_node]
                else:
                    continue

                index = 0
                if len(nodes) == 0:
                    nodes.append((neighbor, distance))

                while nodes[index][1] < distance and index < (len(nodes) - 1):
                    index +=1 
                
                nodes.insert(index, (neighbor, distance))


        # Since we nest O(n) in an O(n) operation, the time complexity of this algorithm
        # is O(n^2)            
        return distances[b]

    def DFS(self, start: int):
        visited_nodes = [False for i in range(self.n)]
        self._DFS(start, visited_nodes)

        return visited_nodes

    def _DFS(self, node, visited):
        if visited[node]:
            return
        visited[node] = True
        for i in range(self.n):
            if self.adj_matrix[node][i] < float("inf"):
                self._DFS(i, visited)
    
    def BFS(self, start):
        q = Queue()
        visited = [False for i in range(self.n)]
        visited[start] = True
        nodes = [start]
        q.add(start)
        while len(q) > 0:
            node = q.remove()
            for i in range(self.n):
                if visited[i]:
                    continue
                else:
                    if self.adj_matrix[node][i] < float("inf"):
                        q.add(i)
                        nodes.append(i)
                        visited[i] = True
        
        return nodes













G = UndirectedWeightedGraph(6)

## Djikstras code 
# G.add(0,1,8)
# G.add(1,4,6)
# G.add(1,2,7)
# G.add(2,3,9)
# G.add(3,4,100)
# G.add(2,5,12)
# print(G.ShortestPath(4,3))

# DFS Code
# print(G.DFS(0))

G.add(0,1,0)
G.add(0,2,0)
G.add(1,3,0)
G.add(2,4,0)
G.add(4,5,0)
G.add(3,5,0)

print(G.BFS(2))
