#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        '''
        Step1: find ordering based on visited time
        Step2: reverse edge
        Step3: start dfs based on visited time
        '''
        
        visited = [False for _ in range(V)]

        # Step1
        time = []
        for i in range(V):
            if not visited[i]:
                self.timedfs(i, visited, time, adj)
                
        
        #Step2
        adjT = [[] for _ in range(V)]
        for f in range(V):
            visited[f] = False # reset visited arr
            for t in adj[f]:
                adjT[t].append(f)
                
        #Step 3
        count = 0
        while time:
            node = time.pop()
            if not visited[node]:
                count += 1
                self.dfs(node, visited, adjT)
        
        
        return count
        
    def timedfs(self, node, visited, time, adj):
        visited[node] = True
        for nb in adj[node]:
            if not visited[nb]:
                self.timedfs(nb, visited, time, adj)
                
        time.append(node)
        
    def dfs(self, node, visited, adj):
        visited[node] = True
        for nb in adj[node]:
            if not visited[nb]:
                self.dfs(nb, visited, adj)
        
        
        