#User function Template for python3

class Solution:
    def kadane(self, arr):
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

    def maximumSumRectangle(self, R, C, M):
        max_sum = float('-inf')

        for i in range(R):
            temp = [0] * C  # Temporary array to store the cumulative sum of columns
            for j in range(i, R):
                # Update the temporary array with the cumulative sum of columns between rows i and j
                for k in range(C):
                    temp[k] += M[j][k]

                # Find the maximum sum subarray in the temporary array using Kadane's algorithm
                current_sum = self.kadane(temp)
                
                # Update the maximum sum if the current_sum is greater
                max_sum = max(max_sum, current_sum)

        return max_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().strip())
    for _ in range(t):
        N,M=map(int,sys.stdin.readline().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,sys.stdin.readline().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.maximumSumRectangle(N,M,a))
# } Driver Code Ends