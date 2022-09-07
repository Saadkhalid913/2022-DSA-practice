from __future__ import annotations
from typing import List, Tuple, Type, Union
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

        while len(nodes) > 0:
            cur_node_tuple = nodes.pop(0)
            cur_node = cur_node_tuple[0]

            visited[cur_node] = True 

            neighbors = self.adj_matrix[cur_node]

            for neighbor, distance in enumerate(neighbors):
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
            
        return distances[b]








G = UndirectedWeightedGraph(6)

G.add(0,1,8)
G.add(1,4,6)
G.add(1,2,7)
G.add(2,3,9)
G.add(3,4,100)
G.add(2,5,12)
print(G.ShortestPath(4,3))