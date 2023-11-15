# User function Template for python3

# User function Template for python3

class Solution:
    def toh(self, N, fromm, to, aux):
        # Your code here
        l,r = 0 , 0
        if N == 0:
            return 0
        if N > 0:
            l = self.toh(N-1,fromm,aux,to)
            print("move disk {} from rod {} to rod {}".format(N, fromm, to))
            r = self.toh(N-1,aux,to,fromm)
        return l + r + 1    


#{ 
 # Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends