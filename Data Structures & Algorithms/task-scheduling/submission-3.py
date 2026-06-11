from collections import Counter,deque
from heapq import heappush,heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = Counter(tasks)
        #heap with (freq,task,timestamp)
        maxHeap,cooldown,time = [],deque(),0
        for key,value in hmap.items():
            heappush(maxHeap,(-value,key,float("-inf")))
        while maxHeap or cooldown:
            time+=1
            while cooldown and cooldown[0][2]+n < time:
                heappush(maxHeap,cooldown.popleft())
            if maxHeap:
                freq,_,timestamp=heappop(maxHeap)
                if -freq-1 > 0:
                    cooldown.append((freq+1,_,time))
        return time


