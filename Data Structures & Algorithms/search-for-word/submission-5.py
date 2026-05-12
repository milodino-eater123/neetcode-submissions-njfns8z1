class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n,m = len(board),len(board[0])
        def aword(i,j,ind,hset):
            nonlocal n,m,board
            if ind>=len(word):
                return True
            if (i,j) in hset:
                return False
            if i<0 or j<0 or i>=n or j>=m:
                return False
            
            
            
            if board[i][j]==word[ind]:
                hset.add((i,j))
                result = aword(i+1,j,ind+1,hset) or aword(i-1,j,ind+1,hset) or aword(i,j+1,ind+1,hset) or aword(i,j-1,ind+1,hset)
                hset.remove((i,j))
                return result
            else:
                return False

            
        
        for i in range(n):
            for j in range(m):
                if aword(i,j,0,set()):
                    return True
        
        return False


        