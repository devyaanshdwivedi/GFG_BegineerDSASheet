#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        ans=[0]
        visited=[-1 for i in range(V)]
        visited[0]=1
        def find(idx):
            temp=adj[idx]
            for i in temp:
                if visited[i]==-1:
                    visited[i]=1
                    ans.append(i)
                    find(i)
        find(0)
        return ans
        # code here
