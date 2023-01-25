class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indx = 0
        for col in zip(*matrix):
            matrix[indx] = reversed(list(col))
            indx += 1
        
        
        