class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #formula to convert coordinates
        #0 to 11
        n = len(matrix)
        m = len(matrix[0])

        low,high = 0, (n*m)-1

        def num(index):
            i = index//m
            j = index%m
            return matrix[i][j]
            
        while high >= low:
            mid = (low+high)//2
            if num(mid) == target:
                return True
            elif num(mid) > target:
                high = mid-1
            else:
                low  = mid + 1 
        
        return False
            
        
        




        