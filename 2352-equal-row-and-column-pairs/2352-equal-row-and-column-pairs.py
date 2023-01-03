class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
    
        for column in zip(*grid):
            for i in range(len(grid)):
                if column == tuple(grid[i]):
                    count += 1
        
        return count
        