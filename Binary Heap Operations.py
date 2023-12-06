#User function Template for python3

'''
heap = [0 for i in range(101)]  # our heap to be used
'''
#Function to insert a value in Heap.

def parent(ind):
    return ((ind - 1)//2)

def left_child(ind):
    return (ind*2)+1


def right_child(ind):
    return (ind*2)+2
    
    
def decrease_key(ind):
    while(ind > 0 and heap[parent(ind)] > heap[ind]):
        heap[ind], heap[parent(ind)] = heap[parent(ind)], heap[ind]
        ind = parent(ind)
        
        
#Function to insert a value in Heap.
def insertKey (x):
    global curr_size
    heap[curr_size] = x
    curr_size += 1
    decrease_key(curr_size-1)
    
    
    

#Function to delete a key at ith index.
def deleteKey(i):
    global curr_size
    if i >= curr_size:
        return
    heap[i] = float('-inf')
    decrease_key(i)
    extractMin()
    


def min_heapify(ind=0):
    
    while True:
        lch_ind = left_child(ind)
        rch_ind = right_child(ind)
        min_ind = ind
        
        if lch_ind < curr_size and heap[lch_ind] < heap[min_ind]:
            min_ind = lch_ind
        
        if rch_ind < curr_size and heap[rch_ind] < heap[min_ind]:
            min_ind = rch_ind
        
        if min_ind != ind:
            heap[min_ind], heap[ind] = heap[ind], heap[min_ind]
            ind = min_ind
        else:
            break
    

#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    global curr_size
    if curr_size == 0:
        return -1
        
    heap[0], heap[curr_size-1] = heap[curr_size-1], heap[0]
    curr_size -= 1
    min_heapify()
    return heap[curr_size]
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

heap = []  # our heap to be used
curr_size = 0  # current size of heap

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        # initialize every globals
        curr_size = 0
        heap = [0 for i in range(n)]
        i = 0
        while i < len(a):
            if a[i] == 1:
                insertKey(a[i + 1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i + 1])
                i += 1
            else:
                print(extractMin (), end=" ")
            i += 1
        # reinitialize every globals
        # curr_size = 0
        # heap = [0 for i in range(101)]
        print()
# } Driver Code Ends