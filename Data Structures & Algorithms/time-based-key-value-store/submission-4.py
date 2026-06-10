from collections import defaultdict
import math
class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        lst = self.hmap[key]
        low,high = 0,len(lst)-1
        while high>low:
            mid = math.ceil((high+low)/2)
            if lst[mid][0]<=timestamp:
                low = mid
            else:
                high = mid -1
        return lst[low][1] if lst and lst[low][0]<=timestamp else ""
        
