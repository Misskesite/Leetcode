# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:36:00 2020

@author: liuga
"""
#时间复杂度O(n+nlogn)-> O(logn) 贪心法 类似于435
class Solution(object):
    def minimumArrows(self, points):
        if not points:
            return 0
        points.sort(key = lambda x:x[1]) #右边排序
        cur_point = points[0][1]
        ans = 1
        for point in range(len(points)):
            if cur_point >= point[0]:
                continue
            cur_point = point[1]
            ans += 1
        return ans
    

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x:x[1]) #右边排序
        arrowX = -math.inf
        ans = 0
        for point in points:
            if point[0] > arrowX:
                
                arrowX = point[1]
                ans += 1
        return ans
