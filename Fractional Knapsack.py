#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        
        ans = 0.0
        for item in arr:
            if W == 0:
                break
            if W < item.weight:
                ans += W * (item.value / item.weight)
                W = 0
                break
            else:
                ans += item.value
                W -= item.weight
        return ans
        # code here