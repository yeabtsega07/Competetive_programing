class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix 
        self.matrix.append([0] * len(matrix[0]))
        
        for row in self.matrix:
            row.append(0)
        
        for  row in range(len(self.matrix) - 1):
            for col in range(len(self.matrix[0]) - 1):
                self.matrix[row][col] += self.matrix[row - 1][col] + self.matrix[row][col - 1] - self.matrix[row - 1][col - 1]
                
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        left = self.matrix[row2][col1 - 1] 
        top = self.matrix[row1 - 1][col2]
        topLeft = self.matrix[row1 - 1][col1 - 1]
        bottomG = self.matrix[row2][col2]
        
        return bottomG - left - top + topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)