class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        max_row, max_col, ans = [], [], 0
        
        for row in grid:
            max_row.append(max(row))
            
        for col in zip(*grid):
            max_col.append(max(col))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur = min(max_row[i], max_col[j])

                if cur != grid[i][j]:
                    ans += cur - grid[i][j]

        return ans