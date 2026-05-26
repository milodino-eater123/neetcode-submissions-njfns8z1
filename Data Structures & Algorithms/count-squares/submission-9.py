from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.dic = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.dic[point]+=1
        

    def count(self, point: List[int]) -> int:
        point = tuple(point)
        res = 0
        x,y = point
        for (i,j),value in self.dic.items():
            if x==i or abs(x-i) != abs(y-j):
                continue
            diag = value
            edge1 = self.dic[(x,j)] if (x,j) in self.dic else 0
            edge2 = self.dic[(i,y)] if (i,y) in self.dic else 0
            res += diag*edge1*edge2
        
        return res

            

        
        
