#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,histogram):
        stack = []
        max_rec = 0
        for index ,bar in enumerate(histogram):
            while stack and bar < histogram[stack[-1]]:
                loc_min_index = stack.pop()
                area = histogram[loc_min_index]*((index-stack[-1]-1) if stack else index)
                max_rec = max(max_rec, area)
            else:
                stack.append(index)
        index = len(histogram)
        while stack:
            top_of_stack = stack.pop()
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_rec = max(max_rec, area)
        return max_rec
                
            
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends