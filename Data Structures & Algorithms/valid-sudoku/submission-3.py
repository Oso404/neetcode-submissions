"""
the hardest part here was finding the square index 
just traverse normally and if already found in that row/col/box return False
like i said hardest part was just finding out the formula for the box
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c = defaultdict(set) #will be updated until the end 
        r = defaultdict(set) #will be updated after each row iteration
        sq = defaultdict(set) #will be updated throughout 


        for rw in range(len(board)):
            for cl in range(len(board[rw])):
                if board[rw][cl] == ".":
                    continue 
                num = board[rw][cl]
                box = (rw//3) * 3 + (cl//3)
                if num in r[rw] or num in c[cl] or num in sq[box]:
                    return False
                r[rw].add(num)
                c[cl].add(num)
                sq[box].add(num)
        return True
                
                                
                
                

        return True