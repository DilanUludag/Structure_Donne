#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Twitter:

    def __init__(self):
        self.tweets = {}  # userId -> list of (timestamp, tweetId)
        self.follows = {}  # userId -> set of followeeIds
        self.time = 0      # global timestamp to keep tweets in order

    def postTweet(self, userId: int, tweetId: int):
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        result = []
        # Get user's tweets
        if userId in self.tweets:
            result.extend(self.tweets[userId])
        # Get tweets from followees
        if userId in self.follows:
            for followeeId in self.follows[userId]:
                if followeeId in self.tweets:
                    result.extend(self.tweets[followeeId])
        # Sort tweets by timestamp and get the 10 most recent
        result.sort(reverse=True, key=lambda x: x[0])
        return [tweetId for _, tweetId in result[:10]]

    def follow(self, followerId: int, followeeId: int):
        if followerId == followeeId:
            return
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int):
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    obj = Twitter()
    totalQueries = int(input ())
    for _ in range (totalQueries):
        query = list(map(int, input().split()))
        if (query[0] == 1):
            userId, tweetId = query[1], query[2]
            obj.postTweet(userId, tweetId)
        elif (query[0] == 2):
            userId =  query[1]
            vec = obj.getNewsFeed(userId)
            for val in vec:
                print(val, end = ' ')
            print()
        elif (query[0] == 3):
            follower, followee = query[1], query[2]
            obj.follow(follower, followee)
        else:
            follower, followee = query[1], query[2]
            obj.unfollow(follower, followee)
# } Driver Code Ends