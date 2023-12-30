
class Solution:
    def findCatalan(self, n : int) -> int:
        # code here
        res = 1
        for i in range(1,n+1):
            res = (res * (4 * i - 2)) // (i + 1)
        return res % (1000000007)
        
        




#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends