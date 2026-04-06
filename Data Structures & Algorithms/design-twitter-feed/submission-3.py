from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweets = []
        self.followed = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        i = len(self.tweets)-1
        while i >= 0:
            if len(res) == 10:
                break
            if self.tweets[i][0] != userId and self.tweets[i][0] not in self.followed[userId]:
                i -= 1
                continue
            res.append(self.tweets[i][1])
            i-=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].discard(followeeId)

        

    #add tweets to one big list
    #get news feed goes down list until getting 10, if not valid continue
    #dic of user ids and followed
