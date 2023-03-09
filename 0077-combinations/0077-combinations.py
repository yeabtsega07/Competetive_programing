class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums =  [ i for i in range( 1, n + 1)]
        
        def backtrack ( nums, index , k , track = []):
            
            if index == len(nums):
                
                if len(track) == k:

                    result.append( track [:] )
                
                return
            
            track.append(nums[index])
            backtrack(nums, index + 1, k, track)
            
            track.pop()
            backtrack(nums, index + 1, k, track)
            
        backtrack(nums, 0, k )
        return result
                    
            