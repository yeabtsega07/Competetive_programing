class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert=0
        for num in nums:
            if num!= val:
                nums[insert]= num
                insert+=1
        return insert          
        