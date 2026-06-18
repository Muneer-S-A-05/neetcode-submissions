class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set) # hashset instead of map to remove O(1)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.time,tweetId])
        self.time -= 1 # we need maxheap to get recent tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []

        # adding all tweets by followee to heap
        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweetmap:
                index = len(self.tweetmap[followeeId])-1 #index of last tweet
                time, tweetId = self.tweetmap[followeeId][index]
                # index-1 to get next element
                # followeeId so we know which list to get it from
                minheap.append([time,tweetId,followeeId,index-1])
        heapq.heapify(minheap)

        # now gonna get the 10 recent ones
        while minheap and len(res)<10:
            time,tweetId,followeeId,index = heapq.heappop(minheap)
            res.append(tweetId)
            if index>=0:
                time, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minheap,[time,tweetId,followeeId,index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)