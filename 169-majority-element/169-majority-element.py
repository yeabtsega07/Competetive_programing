class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans={}
        max_=0
        for n in nums:
            if n not in ans.keys():
                ans[n]=1
            else:
                ans[n]+=1  
            res=n if max_<ans[n] else res    
            max_=max(max_,ans[n])
        
        return res       
       