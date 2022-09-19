class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        col,rows=len(matrix[0]),len(matrix)
        self.mat=[[0]*(col+1)  for r in range(rows+1)]
        for i in range(rows):
            pre=0
            for c in range(col):
                pre+=matrix[i][c]
                top=self.mat[i][c+1]
                self.mat[i+1][c+1]=pre+top
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rear=self.mat[row2+1][col2+1]
        top=self.mat[row1][col2+1]
        lft=self.mat[row2+1][col1]
        toplft=self.mat[row1][col1]
        return rear-top-lft+toplft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)