class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        track = defaultdict(int)
        memo = {1 : 1}
        
        def get_power(num):

            if num in memo:
                return memo[num]
            
            if num % 2:
                ans = 1 + get_power(3 * num + 1)
            else:
                ans = 1 + get_power(num // 2)
            
            memo[num] = ans
            
            return ans
        
        for num in range(lo, hi + 1):
            
            track[num] = get_power(num)
            
        
        return sorted(track.items(), key = lambda x:x[1])[k - 1][0]
            