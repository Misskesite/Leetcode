# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:39:12 2019

@author: liuga
"""
class Interval(object):
    def _init_(self,s=0, e=0):
        self.start = s
        self.end = e
#[[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]        
class Solution(object):
    def mergeIntervals(self, intervals):
        
        intervals.sort(key = lambda x : x.start)
        length = len(intervals)
        res = []
        
        for interval in intervals:
            if res == []:
                res.append(intervals[0]) #第一个区间
                
            else:                
                n = len(res)
                # 有重合
                if res[n-1].start <= interval.start <= res[n-1].end:
                     res[n-1].end = max(interval.end, res[n-1].end)                  
                  
                else:
                     res.append(interval)
                  
        return res
            


class Solution(object):
    def mergeIntervals(self, intervals):
        intervals.sort(key = lambda x : x[0])
        res = []

        for interval in intervals:
            #不重合直接添加, 当前区间与上一个区间不重合
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
            #和上一个区间合并
                res[-1][1] = max(res[-1][1], interval[1])

        return res
