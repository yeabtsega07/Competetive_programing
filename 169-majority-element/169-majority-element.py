class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans={}
        for n in nums:
            if n not in ans.keys():
                ans[n]=1
            else:
                ans[n]+=1       
        
        return max(ans.items(), key=lambda x:x[1])[0]         
       