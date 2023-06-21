# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:00:05 2020

@author: liuga
"""
#排列计算(考虑顺序)
import collections

class Solution(object):
    def numberBoomerage(self, points):
        res = 0
        for p0 in points:
            d = collections.defaultdict(int)
            for p1 in points:
                d[(p0[0]-p1[0])**2 + (p0[1]-p1[1])**2] += 1
            for d, v in d.items(): #for v in d.values():
                res += v*(v-1)
        return res
    
            
'''
如果有n个点和a距离相等，那么排列方式为n(n-1),遍历所有点,让所有的点做点a，计算距离
'''

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x1, y1 in points:
            cnts = defaultdict(int)
            for x2, y2 in points:
                d = (x1 - x2)**2 + (y1 - y2)**2
                ans += 2 * cnts[d]
                cnts[d] += 1
        return ans

