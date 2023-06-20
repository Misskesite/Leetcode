# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:36:21 2019

@author: liuga
"""

class Interval(object):
    def _init_(self,s=0, e=0):
        self.start = s
        self.end = e
        
class Solution(object):
    def insertInterevals(self, intervals, newinterval):
         start, end = newinterval.start, newinterval.end
         left = list(filter(lambda x:x.end < start, intervals )) 
         right = list(filter(lambda x:x.start > end, intervals))

         #有重叠
         if len(left) + len(right) != len(intervals):
             start = min(start, intervals[len(left)].start)
             end = max(end, intervals[-len(right)-1].end)
      
         return left + [Interval(start, end)] + right
        

#第一种方法的简易版
class Solution(object):
    def insertIntervals(self, intervals, newinterval):
        i = 0
        n = len(intervals)
        res = []

        #左边相离的区间
        while i < n and newinterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        tmp = [newInterval[0], newInterval[1]]
        while i < n and newinterval[1] >= intervals[i][0]:
            tmp[0] = min(tmp[0], intervals[i][0])
            tmp[1] = max(tmp[1], intervals[i][1])
            i += 1
        res.append(tmp)

        #右边相离的区间
        while i < n:
            res.append(intervals[i])
            i+=1

        return res

        
            
