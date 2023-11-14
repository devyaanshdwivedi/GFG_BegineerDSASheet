#User function Template for python3

class Solution:
    # Function to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        # Create dictionaries to store character frequencies
        freq_a = {}
        freq_b = {}

        # Count the frequency of characters in string a
        for char in a:
            freq_a[char] = freq_a.get(char, 0) + 1

        # Count the frequency of characters in string b
        for char in b:
            freq_b[char] = freq_b.get(char, 0) + 1

        # Compare the frequency dictionaries
        return freq_a == freq_b


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends