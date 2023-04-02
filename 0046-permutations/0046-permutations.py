class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        track = []
        n = len(nums)
        
        def backtrack (nums, n , cur = []  ):
            
            if len(cur) >= n:
                if len(set(cur)) == n:
                    track.append(cur[:])
                return
            
            for i in range(n):
                
                cur.append(nums[i])
                backtrack(nums, n , cur)
                cur.pop()
        
        
        backtrack( nums, n )
        return track        