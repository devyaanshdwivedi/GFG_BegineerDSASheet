#User function Template for python3



class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        # Code here
        traverse_list=[]
        queue1 = [root]
        while len(queue1)>0:
            current = queue1.pop(0)
            traverse_list.append(current.data)
            if current.left!=None:
                queue1.append(current.left)
            if current.right!=None:
                queue1.append(current.right)
        return traverse_list
        
        
        
        
        
