class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        check = [False] * 3
        t1,t2,t3 = target

        for i,j,k in triplets:
            if i>t1 or j>t2 or k>t3:
                continue
            check[0] = i == t1 or check[0]     
            check[1] = j == t2 or check[1]
            check[2] = k == t3 or check[2]
        
        return all(check)