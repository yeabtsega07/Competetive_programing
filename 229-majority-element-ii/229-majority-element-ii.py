class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        track={}
        for n in nums:
            track[n]=track.get(n,0) +1
        for n in set(nums):
            if track[n]>len(nums)//3:
                ans.append(n)
        return ans        
    
        