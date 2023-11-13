# User function Template for python3
class Solution:

    def findMaximum(self, arr, n):
        # Binary Search to find the peak element
        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2

            # If mid is greater than its neighbors, then mid is the peak
            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
                return arr[mid]
            
            # If the element to the left of mid is greater, then the peak is on the left side
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                high = mid - 1
            
            # If the element to the right of mid is greater, then the peak is on the right side
            else:
                low = mid + 1

        return -1  # If no peak element is found

#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends