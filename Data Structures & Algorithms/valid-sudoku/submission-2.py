class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #doesnt have to be full to be valid just have to go with what we have
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        grids = [[] for _ in range(9)]
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                rows[row].append(board[row][col])
                cols[col].append(board[row][col])
                grids_ind = (row//3) * 3 + (col//3)
                grids[grids_ind].append(board[row][col]) 

        for i in range(9):
            if len(rows[i]) != len(set(rows[i])):
                return False
            if len(cols[i]) != len(set(cols[i])):
                return False
            if len(grids[i]) != len(set(grids[i])):
                return False
        return True

        """
                how to get grid square number of a coordinate?
                0 1 2 
                3 4 5 
                6 7 8
                if rows 0 1 2 --> grid 0 1 2 
                if rows 3 4 5 --> grid 3 4 5 
                if rows 6 7 8 --> grid 6 7 8 

                if cols 0 1 2 --> grid 0 3 6 
                if cols 3 4 5 --> grid 1 4 7
                if cols 6 7 8 --> grid 2 5 8 

                grid 0 --> 0 1 2 , 9 10 11  , 18 19 20
                grid 1 --> 3 4 5 , 12 13 14 , 21 22 23
                grid 2 --> 6 7 8 , 15 16 17 , 24 25 26

                hint 3!

        """



