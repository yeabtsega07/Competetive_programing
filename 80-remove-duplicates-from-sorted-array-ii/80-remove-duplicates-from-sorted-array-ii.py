class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert=0
        dup=1
        for i in range(len(nums)):
            if not insert:
                nums[insert]=nums[i]
                insert+=1
            else:
                if dup and nums[insert-1]==nums[i]:
                    nums[insert]=nums[i]
                    dup=0
                    insert+=1
                elif nums[insert-1]<nums[i]:
                    nums[insert]=nums[i]
                    dup=1
                    insert+=1
        return insert           
            
        