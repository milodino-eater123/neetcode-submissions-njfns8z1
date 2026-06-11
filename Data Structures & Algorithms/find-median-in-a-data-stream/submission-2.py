from heapq import heappush,heappop
class MedianFinder:

    def __init__(self):
        self.lower,self.upper = [],[]
    def addNum(self, num: int) -> None:
        if len(self.lower)<len(self.upper):
            heappush(self.lower,-num)
        else:
            heappush(self.upper,num)
        if self.lower and self.upper and -self.lower[0]>self.upper[0]:
            heappush(self.lower,-heappop(self.upper))
            heappush(self.upper,-heappop(self.lower))
    def findMedian(self) -> float:
        if len(self.upper)>len(self.lower):
            return self.upper[0]
        else:
            return (self.upper[0]-self.lower[0])/2

        
        