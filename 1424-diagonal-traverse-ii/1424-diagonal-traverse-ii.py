class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        
        track = defaultdict(list)
        
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                
                track[row + col].append(nums[row][col])
        
        result = []
        for key in sorted(track.keys()):
            result += reversed(track[key])
        
        return result
        