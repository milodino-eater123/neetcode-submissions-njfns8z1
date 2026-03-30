class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])
        
        def search(i,j,ind):
            nonlocal hmap
            if (i,j) in hmap:
                return False
            if i < 0 or j < 0 or i >= n_rows or j >= n_cols:
                return False
            if board[i][j] != word[ind]:
                return False
            if ind == len(word) - 1:
                return True
            
            hmap.add((i,j))
            result = search(i+1,j,ind+1) or search(i-1,j,ind+1) or search(i,j+1,ind+1) or search(i,j-1,ind+1)
            hmap.remove((i,j))
            return result
        for i in range(n_rows):
            for j in range(n_cols):
                hmap = set()
                if search(i,j,0):
                    return True
        
        return False
        