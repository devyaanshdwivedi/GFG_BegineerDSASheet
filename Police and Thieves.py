#User function Template for python3

class Solution:
    def catchThieves(self, arr, n, k): 
        # code here 
        l1=[]#theif
        l2=[]#police
        for i in range(len(arr)):
            if arr[i]=='T':
                l1.append(i)
            else:
                l2.append(i)
        i=0#police
        j=0#theif
        count=0
        while i<len(l1) and j<len(l2):
            distance=abs(l1[i]-l2[j])
            if distance<=k:
                count+=1
                i+=1
                j+=1
            else:#here u need to think and trick is there . why distance is grtr either due to police or theif?
                if l1[i]>l2[j]:#if police is at larger distance .
                    j+=1
                else:
                    i+=1#if theif is at larger distane
        return count