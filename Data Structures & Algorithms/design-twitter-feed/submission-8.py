from collections import deque,defaultdict
class Twitter:

    def __init__(self):
        self.tweets=deque()
        self.followed = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft((userId,tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for user,tweet in self.tweets:
            if user==userId or user in self.followed[userId]:
                res.append(tweet)
            if len(res)>=10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed[followerId]:
            self.followed[followerId].remove(followeeId)
        
