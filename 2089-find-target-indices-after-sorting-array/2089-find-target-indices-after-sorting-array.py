class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        list_=[]
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if nums[j]<nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        for i in range(len(nums)):
            if nums[i]==target:
                list_.append(i)
        return list_        
        