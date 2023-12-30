#User function Template for python3
import bisect

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        ls = [a[0]]
        
        
        i = 1
        l = 1
        while i < n:
            if a[i] > ls[-1]:
                ls.append(a[i])
                l += 1
            else:
                ind = bisect.bisect_left(ls, a[i])
                ls[ind] = a[i]
            i+=1
            
        return l
       

