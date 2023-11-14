class Solution:
    def count(self, coins, N, Sum):
        # Initializing dp array to store the number of ways to make change for each sum
        dp = [0] * (Sum + 1)
        dp[0] = 1  # There is one way to make change for sum 0, i.e., by not selecting any coin

        # Iterate over each coin
        for coin in coins:
            # Iterate over each sum from the coin value to the target sum
            for j in range(coin, Sum + 1):
                # Update the dp array with the sum of ways to make change
                dp[j] += dp[j - coin]

        # The final result is stored in dp[Sum]
        return dp[Sum]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends