class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        # Check if left child exists and is greater than root
        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        # Check if right child exists and is greater than root
        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        # Swap the root if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # Recursively heapify the affected sub-tree
            self.heapify(arr, n, largest)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        # Build a max heap from the bottom-up
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        # Build the initial heap
        self.buildHeap(arr, n)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap the root with the last element
            self.heapify(arr, i, 0)  # Heapify the reduced heap


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends