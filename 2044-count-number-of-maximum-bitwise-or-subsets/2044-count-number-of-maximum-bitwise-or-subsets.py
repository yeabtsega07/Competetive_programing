class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        track = defaultdict( int )
        
        def backtrack ( nums, index = 0, cur = [] ):
            
            if index == len(nums):
                
                check = 0
                for  num in cur:
                    check |= num
                
                track[check] += 1
                
                return
            
            cur.append(nums[index])
            backtrack( nums, index + 1, cur )
            cur.pop()
            
            backtrack( nums, index + 1, cur)
        
        backtrack( nums )
        return track[ max( track.keys() ) ]
        