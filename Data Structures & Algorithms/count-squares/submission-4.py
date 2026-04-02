from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.dic = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.dic[tuple(point)] += 1 
        

    def count(self, point: List[int]) -> int:
        point = tuple(point)
        res,visited=0,set()
        points = set(self.dic.keys())
        for key in points:
            x,y=key
            if abs(x-point[0])!=abs(y-point[1]) or key==point:
                continue
            first,second = (point[0],y),(x,point[1])
            if first in points and second in points:
                newSquare = tuple(sorted((key,point,first,second)))
                if newSquare in visited:
                    continue
                num = self.dic[key] * self.dic[first]*self.dic[second]
                res += num
                visited.add(newSquare)
        return res

            #(x,y)

            #(x,y),(x,y+4)

            #(x,y),(x,y+4),(x-4,y+4)

            #(x,y),(x,y+4),(x-4,y+4),(x-4,y)

            #if valid, look for set

            #if set is valid, add to res, then add to visited


            

        
