class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x,y = len(board),len(board[0])
        rows = [set() for x in range(9)] 
        cols = [set() for x in range(9)] 
        boxes = [set() for x in range(9)] 

        for i in range(x):
            for j in range(y):
                k = i//3*3 + j // 3
                num = board[i][j]
                if num == ".":
                    continue
                
                if num in rows[i] or num in cols[j] or num in boxes[k]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[k].add(num)
        
        return True
        