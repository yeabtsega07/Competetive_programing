class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            l = [0]*9
            for j in range(9):
                if board[i][j]!=".":
                    if l[int(board[i][j])-1] == 1:
                        return 0
                    else:
                        l[int(board[i][j])-1] = 1



        for i in range(9):
            l = [0]*9
            for j in range(9):
                if board[j][i]!=".":
                    if l[int(board[j][i])-1] == 1:
                        return 0
                    else:
                        l[int(board[j][i])-1] = 1




        for i in range(0,9,3):
            for j in range(0,9,3):
                l = [0]*9
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if board[x][y]!=".":
                            if l[int(board[x][y])-1] == 1:
                                return 0
                            else:
                                l[int(board[x][y])-1] = 1
                                
        return board
        