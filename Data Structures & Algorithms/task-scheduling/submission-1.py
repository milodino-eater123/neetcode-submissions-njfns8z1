from collections import defaultdict,deque
from heapq import heappush,heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #populate hmap
        hmap = defaultdict(int)
        for task in tasks:
            hmap[task] += 1 
        
        #convert hmap's values into max heap
        heap = []
        for key,value in hmap.items():
            heappush(heap,[-value,key])
        
        #initialise
        cooldown = deque()
        timestamp = 0

        #iterate through tasks
        while heap or cooldown:
            timestamp += 1 
            #check tasks on cooldown
            while cooldown:
                if timestamp - cooldown[0][-1] < n+1:
                    break
                temp = cooldown.popleft()
                temp.pop()
                heappush(heap,temp) 
            #do task from heap of available tasks
            if heap:
                lst = heappop(heap)
                lst[0] += 1 
                if lst[0] < 0:
                    lst.append(timestamp)
                    cooldown.append(lst)
        
        return timestamp
    


        