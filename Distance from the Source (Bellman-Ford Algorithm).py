#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        
        visited = [10**8]*V
        visited[S] = 0
        for i in range(V-1):
            for src, dest, wt in edges:
                if visited[src] != 10**8 and visited[dest] > visited[src]+wt:
                    visited[dest]= visited[src]+wt

        for src, dest, wt in edges:
            if visited[src] != 10**8 and visited[dest] > visited[src]+wt:
                return [-1]
        
        return visited

