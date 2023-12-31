#User function Template for python3

class Disjoint:
    def __init__(self,n):
        self.size=[1]*(n+1)
        self.parent=[i for i in range(n+1)]
        
    def findparent(self,nod):
        if self.parent[nod]!= nod:
            self.parent[nod]=self.findparent(self.parent[nod])
        return self.parent[nod]
        
        
    def unionbysize(self,u,v):
        u_par = self.findparent(u)
        v_par = self .findparent(v)
        if u_par == v_par:
            return
        
        if self.size[u_par] < self.size[v_par]:
            self.parent[u_par]=v_par
            self.size[v_par]+=self.size[u_par]
            
        else:
            self.parent[v_par]=u_par
            self.size[u_par]+=self.size[v_par]
            
        
        
class Solution:
    def numProvinces(self, adj, V):
        ds = Disjoint(V)
        
        for a in range(V):
            for b in range(V):
                if adj[a][b]==1:
                    ds.unionbysize(a,b)
                    
                
                
        count=0
        for i in range(V):
            if ds.parent[i]==i:
                count+=1
                
        return count    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends