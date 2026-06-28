from collections import defaultdict
from heapq import heappush,heappop
class Twitter:
    def __init__(self):
        self.tweets=defaultdict(list)
        self.followed=defaultdict(set)
        self.time=0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res,minHeap = [],[]
        followed = self.followed[userId]|{userId}
        for followee in followed:
            dq = self.tweets[followee]
            if dq:
                time,id=dq[-1]
                heappush(minHeap,(time,id,followee,len(dq)-2))
        while minHeap and len(res)<10:
            _,id,user,j=heappop(minHeap)
            res.append(id)
            if j>=0:
                time,id=self.tweets[user][j]
                heappush(minHeap,(time,id,user,j-1))
        return res

        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].discard(followeeId)
        
