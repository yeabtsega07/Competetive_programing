class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums

        cnt={}
        for i,n in enumerate(nums):
            if n not in cnt.keys():
                cnt[n]=1
            else:
                cnt[n]+=1
             
        res=[]
        for i in set(nums):
            if i+1 not in cnt.keys() and i-1 not in cnt.keys() and cnt[i]==1:
                res.append(i)
 
        
        return res
    
                
                
        