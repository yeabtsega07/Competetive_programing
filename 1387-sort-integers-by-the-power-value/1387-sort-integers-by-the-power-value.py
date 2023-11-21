class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        memo = {1:0}
        
        def get_power(num):
            
            if num in memo:
                return memo[num]
            
            if num % 2:
                cur = 1 + get_power(num * 3 + 1)
            else:
                cur = 1 + get_power(num // 2)
            
            return cur
        
        nums = {}
        
        for num in range(lo, hi + 1):
            
            nums[num] = get_power(num)
        
        nums = sorted(nums.items(), key = lambda x:x[1])

        return nums[k - 1][0]
            