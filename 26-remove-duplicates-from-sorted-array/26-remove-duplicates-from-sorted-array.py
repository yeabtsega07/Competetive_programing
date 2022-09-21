class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert=0
        for i in range(len(nums)):
            if not insert:
                nums[insert]=nums[i]
                insert+=1
            else:
                if nums[insert-1]<nums[i]:
                    nums[insert]=nums[i]
                    insert+=1
        return insert            
            
   
        