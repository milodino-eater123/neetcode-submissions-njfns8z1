from collections import defaultdict
from heapq import heappush,heappop
class Twitter:

    def __init__(self):
        self.followed = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 100000
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp,tweetId))
        if len(self.tweets[userId]) > 10:
                self.tweets[userId].pop(0)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #make max heap
        #take first min value from each and add
        #pop max value, add to res
        #take min value from same followee
        #stop at 10
        res = []
        maxHeap = []
        if self.tweets[userId]:
            myTimestamp,myTweetid = self.tweets[userId][-1]
            maxHeap.append((-myTimestamp,userId,myTweetid,-1))

        for followed in self.followed[userId]:
            if followed == userId:
                continue
            if self.tweets[followed]:
                timestamp,tweetid = self.tweets[followed][-1]
                heappush(maxHeap,(-timestamp,followed,tweetid,-1))
        
        while maxHeap:
            timestamp,user,tweet,i = heappop(maxHeap)
            res.append(tweet)
            if -i+1 <= len(self.tweets[user]):
                newTimestamp,newTweet = self.tweets[user][i-1]
                heappush(maxHeap,(-newTimestamp,user,newTweet,i-1))
            if len(res) >= 10:
                return res
        
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].discard(followeeId)

        
