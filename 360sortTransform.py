# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:21:34 2020

@author: liuga
"""
import heapq

class Solution(object):
    def sorttransform(nums, a,b,c):
        res = []
        q = []
        heapq.heapify(q)
        
        for n in nums:
            heapq.heappush(q, a*n*n+b*n+c)
            
        while q:
            res.append(heapq.heappop(q))
        
        return res