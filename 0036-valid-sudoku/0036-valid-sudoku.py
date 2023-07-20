class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        // spacing + indentation 👍

        for row in range(9):
            l = [0]*9
            for col in range(9):
                if board[row][col]!=".":
                    if l[int(board[row][col])-1] == 1:
                        return 0
                        # if you are returning - you don't need else
                    # else:
                    l[int(board[row][col])-1] = 1
        # if's better to use more descriptive variable names
        for row in range(9):
            l = [0]*9
            for col in range(9):
                if board[col][row]!=".":
                    if l[int(board[col][row])-1] == 1:
                        return 0
                        # same here...if you are returning sth - NO ELSE WILL BE NEEDED
                    # else:
                    l[int(board[col][row])-1] = 1

        # variable naming- descriptive
        for row in range(0,9,3):
            for col in range(0,9,3):
                l = [0]*9
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if board[x][y]!=".":
                            if l[int(board[x][y])-1] == 1:
                                return 0
                            else:
                                l[int(board[x][y])-1] = 1
                                
        return board
        
