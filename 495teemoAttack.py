# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:16:11 2020

@author: liuga
"""
#比较相邻两个时间点的时间差，如果小于duration，就加上这个差，如果大于或等于，就加上duration即可
class Solution(object):
    def teemoAttack(self, timeSerials, duration):
        if not timeSerials:
            return 0
        total = duration*len(timeSerials)
        for i in range(1, len(timeSerials)):
            if timeSerials[i] < timeSerials[i-1]+ duration:
                total -= timeSerials[i-1] + duration - timeSerials[i]
        return total
     #改写
    
    n = len(timeSerials)
    res  = 0
    for i in range(1, n): #统计的是上次中毒的时间
        if duration > timeSerials[i] - timeSerials[i-1]:
            res += timeSerials[i] - timeSerials[i-1]
        else:
            res += duration
    
    res += duration #最后一次中毒
