class Solution:
    # Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, a, n):
        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                a[i][j], a[j][i] = a[j][i], a[i][j]

        # Reverse each column of the transposed matrix
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                a[left][i], a[right][i] = a[right][i], a[left][i]
                left += 1
                right -= 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()

# } Driver Code Ends