class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        import heapq
        distances = [float('infinity')]*V
        distances[S] = 0

        pq = [(0, S)]  # (distance from S to S=0, starting node)
        
        while(len(pq) > 0):  # till pqueue is empty
            current_distance, current_vertex = heapq.heappop(pq)

            # Nodes can get added to the priority queue multiple times. We only
            # process a vertex the first time we remove it from the priority queue.
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in adj[current_vertex]:
                distance = current_distance + weight
                # new smaller path has been discovered, add it to pq so that all
                # its neighbours can be recalculated
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends