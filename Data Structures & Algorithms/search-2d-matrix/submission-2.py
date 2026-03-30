class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        total = n_rows * n_cols - 1 


        #approach 1: convertor
        def convertor(n):
            quotient = n // n_cols 
            remainder = n % n_cols
            return matrix[quotient][remainder]
            
        low,high = 0,total

        while high >= low:
            mid = (high+low)//2
            mid_val = convertor(mid)
            if target == mid_val:
                return True
            elif target > mid_val:
                low = mid + 1 
            else:
                high = mid - 1 
        
        return False




        