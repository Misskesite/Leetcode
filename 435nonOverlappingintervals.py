# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:15:58 2020

@author: liuga
"""
#首个区间就是所有可以选择的区间中右端点最小的那个区间 时间复杂度O(nlogn + n) -> O(nlogn)
class Solution(object):
    def eraseOverlapping(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        prev = 0
        res = 0
        for i in range(1, len(intervals)):
            if intervals[prev].end > intervals[i].start:
                if intervals[i].end < intervals[prev].end: #新区间终点更靠前
                    prev = i
                res += 1
            else:
                prev = i
        return res
        
#A classic greedy case: interval scheduling problem. always pick the interval with the earliest end time. Then you can get the maximal number of non-overlapping intervals.
#This is because, the interval with the earliest end time produces the maximal capacity to hold rest intervals.
#贪心算法，按照右边排序, 类似会议室安排
class Solution(object):
    def eraseOverlap(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1 #ans 不重合的个数？
                right = intervals[i][1]
        return n - ans
                
