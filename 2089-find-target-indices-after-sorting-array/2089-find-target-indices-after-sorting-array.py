class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        final=[]
        for i in range (len(nums)-1):
            m_val=min(nums[i:])
            m_in=nums.index(m_val,i)
            if nums[i]!=nums[m_in]:
                nums[i],nums[m_in]=nums[m_in],nums[i]
        for i in range(len(nums)):
            if nums[i]==target:
                final.append(i)
        return final        
         