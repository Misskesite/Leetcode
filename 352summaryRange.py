# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:05:27 2020

@author: liuga
"""
#类似于57 insert interval , the data stream are 1 3 7 2 6
[1,1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
#follow up, what if there are lots of merges and numer of disjoint inervals are small

class solution(object):
    def summaryrange(intervals):
        
        def addNum(val,intervals):
            newInterval = []
            res = []
            cur = 0
            for interval in intervals:
                if newInterval[1]+1 < interval[0]:
                    res.append(interval)
                elif newInterval[0] > interval[1] + 1:
                    res.append(interval)
                    cur += 1
                else:
                    newInterval[0] = min(newInterval[0], interval[0])
                    newInterval[1] = max(newInterval[1], interval[1])
            res.insert(res[0] + cur, newInterval)
            intervals = res
            return res
        
#此解法为主
class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, val: int) -> None: # O(logn)
        bisect.insort(self.intervals, (val, val))
        
    def getIntervals(self) -> List[List[int]]: #O(n)
		# similar as 56, but since the intervals are inserted in ordered order, we donot need to sort it
		# the time complexity would just O(n), 
		# since prepare the result will need O(n), it will not increase the time complexity
        stack = []
        for start, end in self.intervals:   #
            if stack and start <= stack[-1][1]  + 1:
                stack[-1][1] = max(stack[-1][1], end)
            else:
                stack.append([start, end])
        self.intervals = stack
        return self.intervals
            


                
'''
每进来一个新的数字 val，都生成一个新的区间 [val, val]，并且新建一个空的区间数组 res，用一个变量 cur 来保存要在现有的区间数组中加入新区间的位置
'''

class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        self.seen = set()

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """      
        if val not in self.seen:
            self.seen.add(val)
            heapq.heappush(self.intervals, [val, val])
        
    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        
        tmp = []

        while self.intervals: #全局变量
            cur = heapq.heappop(self.intervals)
            if tmp and cur[0] <= tmp[-1][1] + 1:
                tmp[-1][1] = max(tmp[-1][1], cur[1])
            else:
                tmp.append(cur)

        self.intervals = tmp
        return self.intervals
    
        
#并查集 集合的父亲代表该联通集的右边界
from sortedcontainers import SortedSet
class Solution2(object):
    def _init_(self):
        self.f = [i for i in range(10002)]
        self.points = SortedSet()

    def addNum(self, val: int) -> None:
        self.points.add(val)
        self.f[val] = self.f[val + 1]

    def getIntervals(self) -> List[List[int]]:
        ans = []
        for p in self.points:
            if ans and p <= ans[-1][1]:
                continue
            ans.append([p, self.find(p) - 1])
        return ans
    
    def find(self, x):
        if x == self.f[x]:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    
#更规范容易懂 数据流变成多个不相交的区间
class SummaryRanges:

    def __init__(self):
        self.f = list(range(10001))
        self.ans = {} #左边界存在字典里？

    def find(self, i):
        if i != self.f[i]:
            self.f[i] = self.find(self.f[i])
        return self.f[i]

    def union(self, i, j):
        fi, fj = self.find(i), self.find(j)
        if fi != fj:
            self.f[fj] = fi
            self.ans[fi] += self.ans[fj]
            del self.ans[fj]

    def addNum(self, val: int) -> None:
        if self.find(val) in self.ans:
            return
        self.ans[val] = 1
        if val > 0 and self.find(val - 1) in self.ans: #该数字的前一个和后一个已经存在
            self.union(val - 1, val) #合并左边
        if val < 10000 and self.find(val + 1) in self.ans:
            self.union(val, val + 1) #合并右边

    def getIntervals(self) -> List[List[int]]:
        return sorted([[i, i + j - 1] for i, j in self.ans.items()]) #j是区间长度？
    

        

from bisect import bisect_left

class SummaryRanges:

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.interval = [] # record the interval
    self.s = set() # record the number we have added before
    return 

def addNum(self, val: int) -> None:
    if val in self.s:
        return 
    self.s.add(val)
    index = bisect_left(self.interval,[val,val])
    
    # check whether we could extend the interval on its left and right 
    if index < len(self.interval) and self.interval[index][0]-1 == val:
        self.interval[index][0] = self.interval[index][0] - 1
    elif index > 0 and self.interval[index-1][1]+1 == val:
        self.interval[index-1][1] = self.interval[index-1][1] + 1
    else:
        self.interval.insert(index, [val,val])

def getIntervals(self) -> List[List[int]]:
    # update the intervals in getIntervals function 
    tmp = []
    for cur in self.interval:
        if tmp and tmp[-1][1] == cur[0]-1:
            tmp[-1][1] = cur[1]
        else:
            tmp.append(cur)
    self.interval = tmp
    return self.interval

#改写

def addNum(self, val: int) -> None:
    if val in self.s:
        return 
    self.s.add(val)
    index = bisect_left(self.interval,[val,val])

    self.interval.insert(index, [val,val])
    
    # check whether we could extend the interval on its left and right 
    if index + 1 < len(self.interval) and self.interval[index + 1][0] == val + 1:
        self.interval[index][1] = self.interval[index+1][1]
        del self.interval[index + 1]
    if index -1 >= 0 and self.interval[index-1][1] == val - 1:
        self.interval[index-1][1] = self.interval[index][1]
        del self.interval[index]
    
        

def getIntervals(self) -> List[List[int]]:
    
    return self.interval

''




