class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = list(set(nums))
        check.sort()
        for i in range(len(nums)):
            if i < len(check):
                nums[i] = check[i]
        
        return len(check)
            