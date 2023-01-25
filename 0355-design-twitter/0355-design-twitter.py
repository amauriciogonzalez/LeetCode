class Twitter(object):

    def __init__(self):
        self.time = 0
        self.usersToTweets = defaultdict(list) # user : [time, tweetID] list
        self.usersToFollowers = defaultdict(set) # user : follow hashSet
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.usersToTweets[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        result = []
        observedTweets = []
        heapq.heapify(observedTweets)
        self.usersToFollowers[userId].add(userId)
        for followeeId in self.usersToFollowers[userId]:
            if followeeId in self.usersToTweets:
                lastIndex = len(self.usersToTweets[followeeId]) - 1
                time, tweetId = self.usersToTweets[followeeId][lastIndex]
                heapq.heappush(observedTweets, [time, tweetId, followeeId, lastIndex - 1])

        while observedTweets and len(result) < 10:
            print(observedTweets)
            time, tweetId, followeeId, index = heapq.heappop(observedTweets)
            result.append(tweetId)
            if index >= 0:
                time, tweetId = self.usersToTweets[followeeId][index]
                heapq.heappush(observedTweets, [time, tweetId, followeeId, index - 1])
        return result

        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.usersToFollowers[followerId].add(followeeId)
        
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.usersToFollowers[followerId]:
            self.usersToFollowers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)