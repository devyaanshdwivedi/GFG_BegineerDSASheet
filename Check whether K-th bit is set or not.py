#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    
    # Function to check if Kth bit is set or not.
    def checkKthBit(self, n, k):
        # Left shift 1 by k positions to create a mask with the kth bit set.
        mask = 1 << k
        
        # Check if the kth bit is set by ANDing n with the mask.
        # If the result is non-zero, the kth bit is set; otherwise, it is not set.
        return (n & mask) != 0

#{ 
 # Driver Code Starts.


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        obj = Solution()
        if obj.checkKthBit(n,k):
            print("Yes")
        else:
            print("No")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends