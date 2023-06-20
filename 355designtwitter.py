# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:07:36 2020

@author: liuga
"""

import collections
import heapq
import itertools

class Twitter(object):
    def _init_(self):
        self.timer = itertools.count(step = -1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userID].appendleft(next(self.timer), tweeId)


    def getNewsFeed(self, userId):
        #userId需要并上自己的推文，至多取前10项
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)

#上面方法改写
class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(list)
        self.tweets_time = defaultdict(list)
        self.time = 0
        self.follows = defaultdict(set)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].insert(0, tweetId)
        self.tweets_time[userId].append([self.time, tweetId])
        self.time+=1

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news = self.tweets_time[userId].copy()
        for f in self.follows[userId]:
            news+=self.tweets_time[f]
        if news: 
            news.sort(key=lambda x:x[0], reverse=True)
            return [t[1] for t in news][0:10]
        else: 
            return []

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follows[followerId]: 
            self.follows[followerId].remove(followeeId)

'''
postTweet(userId, tweetId) : Compose a new tweet.
getNewsFeed(userId) : Retrieve the 10 most recent tweet ids in the user’s news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId) : Follower follows a followee.
unfollow(followerId, followeeId) : Follower unfollows a followee.

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);

'''

class Twietter:
    def _init_(self):
        self.count = 0
        self.tweetMap = defaultdict(list) #userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) #userId -> set of followeeId

    def postTweet(self, userId:int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int)-> List[int]:
        res = []  #ordered starting from recent
        minHeap = []

        self.followMap[userId].add(userId) #添加自己的
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap: #保证至少有一个twitter
                index = len(self.tweetMap[followeeId]) - 1
                count, tweerId = self.tweetMap[followeeId][index] #count is unique
                minHeap.append([count,tweetId, followeeId, index - 1])
        heapq.heaify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heapop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, folloeeId, index -1])

    def follow(self, foloowId, followeeId) ->None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
