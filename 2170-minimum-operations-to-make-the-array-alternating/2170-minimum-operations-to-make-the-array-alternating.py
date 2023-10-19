class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            if len(nums) == 2 and nums[1] == nums[0]:
                return 1
            return 0
        
        evens = defaultdict(int)
        
        for i in range(0, len(nums), 2):
            evens[nums[i]] += 1
        
        odds = defaultdict(int)
        
        for i in range(1, len(nums), 2):
            odds[nums[i]] += 1
        
        odd_vals = sorted(odds.items(), key = lambda x:x[1], reverse = True)
        even_vals = sorted(evens.items(), key = lambda x:x[1], reverse = True)
        
        if even_vals[0][0] != odd_vals[0][0]:
            count, cur = 0, (even_vals[0][0], 1)
            for num in nums:
                if num != cur[0]:
                    count += 1
                cur = (odd_vals[0][0], 0) if cur[1] else (even_vals[0][0], 1)
            
            return count
            
        else:
            count1 = 0
            if len(odd_vals) > 1:
                cur = (even_vals[0][0], 1)
                for num in nums:
                    if num != cur[0]:
                        count1 += 1
                    cur = (odd_vals[1][0], 0) if cur[1] else (even_vals[0][0], 1)
            else:
                cur = (even_vals[0][0], 1)
                for num in nums:
                    if num != cur[0]:
                        count1 += 1
                    cur = (-1, 0) if cur[1] else (even_vals[0][0], 1)
            count2 = 0
            if len(even_vals) > 1:
                cur = (even_vals[1][0], 1)
                for num in nums:
                    if num != cur[0]:
                        count2 += 1
                    cur = (odd_vals[0][0], 0) if cur[1] else (even_vals[1][0], 1)
            else:
                cur = (-1, 1)
                for num in nums:
                    if num != cur[0]:
                        count2 += 1
                    cur = (odd_vals[0][0], 0) if cur[1] else (-1, 1)
                
            count1 = float("inf") if not count1 else count1
            count2 = float("inf") if not count2 else count2
            
            return min(count1, count2)
            
        
        