from heapq import heappush,heappop
class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.bigger = []
        

    def addNum(self, num: int) -> None:
        if len(self.bigger) < len(self.smaller):
            heappush(self.bigger,num)
        else:
            heappush(self.smaller,-num)
        
        if self.bigger and self.bigger[0] < -self.smaller[0]:
            temp1,temp2 = heappop(self.bigger),-heappop(self.smaller)
            heappush(self.smaller,-temp1)
            heappush(self.bigger,temp2)
        

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.bigger):
            return -self.smaller[0]
        else:
            return (-self.smaller[0]+self.bigger[0])/2
        
        