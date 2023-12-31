#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        from typing import List
from queue import Queue

class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        bfs = []
        visited = [False] * V
        queue = Queue()
        queue.put(0)
        visited[0] = True
        while not queue.empty():
            node = queue.get()
            bfs.append(node)
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    queue.put(neighbour)
                    visited[neighbour] = True
        return bfs
