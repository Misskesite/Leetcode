# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:00:52 2020

@author: liuga
"""

class Solution(object):
    def findMinimumdifference(self, timePoints):
        
        def convert(time):
            return int(time[:2]*60 + time[3:])
        
        timePoints = map(convert, timePoints)
        timePoints.sort()
        return min((y-x)*(24*60) for x, y in zip(timePoints[1:] +  timePoints[:1]))
    
    
#分钟数组排序之后，最小时间差一定是数组中的两个相邻时间之差，或者数组的首元素与末元素之差加上 1440（一天的分钟数是 1440）
class Solution2(object):
    def findMinimumdifference(self, timePoints):
        for i, time in enumerate(timePoints):
            hour, minutes = times.split(':')
            min_past_midnight = int(hours)*60 + int(minutes)
            timePoints[i] = min_past_midnight
        timePoints.sort()
        res = 1440 + timepoints[0] - timepoints[-1] #normalize 第一个和最后一个时间差
        for i in range(1, len(timePoints)):
            res = min(res, timePoints[i] - timePoints[i-1])

        return res
            
