from collections import defaultdict
import math
class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap or self.hmap[key][0][0]>timestamp:
            return ""
        lst = self.hmap[key]
        low,high=0,len(lst)-1
        while high>low:
            mid = math.ceil((low+high)/2)
            if timestamp==lst[mid][0]:
                low = mid
                break
            elif timestamp>lst[mid][0]:
                low = mid 
            elif timestamp<lst[mid][0]:
                high = mid-1
        return lst[low][1]



        
