class Solution:
    def insert(self, alist, index, n):
        key = alist[index]
        j = index - 1

        # Move elements greater than key to one position ahead of their current position
        while j >= 0 and key < alist[j]:
            alist[j + 1] = alist[j]
            j -= 1

        # Place key at its correct position in sorted array
        alist[j + 1] = key

    def insertionSort(self, alist, n):
        for i in range(1, n):
            # Insert the element at index i in the sorted part of the array
            self.insert(alist, i, n)

#{ 
 # Driver Code Starts

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends