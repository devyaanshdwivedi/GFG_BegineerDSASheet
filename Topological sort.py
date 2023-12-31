from collections import deque
class Solution:
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indegree=[0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        q=deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        top=[]
        while(q):
            node=q.popleft()
            top.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
            
        return top