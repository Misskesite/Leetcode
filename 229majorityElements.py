# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 16:24:09 2019

@author: liuga
"""
import collections
class Solution(object):
    def majorityelement(self, nums):
        n = len(nums)
        count = collections.Counter(nums)
        res = []
        for n, t in count.items():
            if t > n//3:
                res.append(n)
        return res
        
