# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:41:25 2020

@author: liuga
"""
#时间复杂度O(n)
#直线对称 存在一条平行为Y的直线，使得所有的点关于该直线对称
#[[1, 1], [-1, 1]] true. [[1,1] ,[-1, -1]] False
class Solution(object):
    def isreflected(self, points):
        mp = {}
        mx = 0
        mn = 0
        for p in points:
            mx = max(mx, p[0])
            mn = min(mn, p[0])
            mp[p[0]].add(p[1])
        mid = (mn + mx)/2
        for p in points:
            t = 2*mid - p[0] #通过一个点，对称的线，找到对面的点
            if not mp.ge(t,0) or not mp[t].get(p[1],0): #p[1] in mp[t]?
                return False
        return True

#考虑有个点在中垂线上？
#此解法为主    
class Solution:
  def isReflected(self, points: List[List[int]]) -> bool:
    minX = math.inf
    maxX = -math.inf
    seen = set()

    for x, y in points:
      minX = min(minX, x)
      maxX = max(maxX, x)
      seen.add((x, y))

    summ = minX + maxX
    # (leftX + rightX) / 2 = (minX + maxX) / 2
    #  leftX = minX + maxX - rightX
    # RightX = minX + maxX - leftX

    return all((summ - x, y) in seen for x, y in points)
