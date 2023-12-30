#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
         ans=[]
         x=int(0)
         y=int(1)
         while n>0:
             x,y=y,x+y
             ans.append(x)
             n-=1
         return ans     