class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        myMap = defaultdict(int)
        
        for row in range(9):
            for col in range(9):
                if board[row][col]!=".":
                    myMap[(row,col)] = board[row][col]
        
        # check for validity
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                # check for valid - row
                for i in range(9):
                    if i != col and myMap[(row, i)] == val:
                        return False
                # check for valid - col
                for i in range(9):
                    if i!=row and myMap[(i, col)] == val:
                        return False
                
                # check for 3x3 neighbors:
                start_row = (row//3)*3
                start_col = (col//3)*3
                for i in range(3):
                    for j in range(3):
                        current_row = start_row+i
                        current_col = start_col+j
                        if not (current_row == row and current_col == col):
                            if myMap[(current_row, current_col)] == val:
                                return False
                
        return True
                    