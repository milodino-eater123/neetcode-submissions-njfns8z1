from collections import Counter,deque
from heapq import heappush,heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = Counter(tasks)
        #heap with (freq,task,timestamp)
        maxHeap,cooldown,time = [],deque(),0
        for value in hmap.values():
            heappush(maxHeap,-value)
        while maxHeap or cooldown:
            time+=1
            while cooldown and cooldown[0][1]+n<time:
                heappush(maxHeap,cooldown.popleft()[0])
            if maxHeap:
                freq=heappop(maxHeap)
                if -freq-1 > 0:
                    cooldown.append((freq+1,time))
        return time


