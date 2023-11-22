class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        track = defaultdict(list)
        
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                
                track[row + col].append(nums[row][col])
        

        result, even = [], 0
        for key in sorted(track.keys()):
            if even:
                result += track[key]
                even = 0
            else:
                result += reversed(track[key])
                even = 1
        
        return result