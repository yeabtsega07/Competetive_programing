class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        left, right = 0, len(nums) - 1
        
        while right >= left:
            if nums[right] + nums[left] > target:
                right -= 1
            
            else:
                
                res += 2**(right - left)
                left += 1
        
        # print(res)
        return res % (10**9 + 7)        
        

        