#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Twitter:

    def __init__(self):
        self.tweets = {}  # clef = userId , donnée =  list de (timestamp, tweetId) (dictionnaire)
        self.follows = {}  # clef = userId, donnée =  followeeIds  (dictionnaire)
        self.time = 0      # compteur global pour l'ordre des tweets

    def postTweet(self, userId, tweetId): #permets de poster un tweet

        if userId not in self.tweets: # si l'utilisateur n'a jamais fait de tweet
            self.tweets[userId] = [] # on ajoute la clef au dictionnaire avec aucune donnée

        self.tweets[userId].append((self.time, tweetId)) # ajoute la donnée à la clef associé à son nom
        self.time += 1 # augmente le timestamp

    def getNewsFeed(self, userId ): # renvoie les 10 tweets les plus récents
        result = []
        # On cherche les tweet de lui même
        if userId in self.tweets:
            result.extend(self.tweets[userId])


        # On prends les tweets de ses folowers
        if userId in self.follows:
            # pour tout ses abonnements
            for followeeId in self.follows[userId]:
                # si ses abonnements ont tweet quelques chose
                if followeeId in self.tweets:
                    # ajout au result
                    result.extend(self.tweets[followeeId])

        # trie par time
        result.sort(reverse=True, key=lambda x: x[0])

        # prends les 10 premiers
        return [tweetId for _, tweetId in result[:10]]



    def follow(self, followerId , followeeId ):
        if followerId == followeeId: # si on veut s'abonner a soi meme
            return

        if followerId not in self.follows: #si il est abonné a personne
            self.follows[followerId] = set()  #ajoute au dictionnaire sans donnée

        self.follows[followerId].add(followeeId) # ajoute l'abonnement

    def unfollow(self, followerId, followeeId):
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId) # on supprime

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