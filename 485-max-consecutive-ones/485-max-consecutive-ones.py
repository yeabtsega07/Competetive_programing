class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones=0
        count=0
        for i in nums:
            if i==1:
                count+=1
            else:
                ones=max(ones,count)
                count=0
        ones=max(ones,count)        
        return ones        