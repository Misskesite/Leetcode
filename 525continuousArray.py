# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:06:29 2020

@author: liuga
"""

class Solution(object):
    def findmaxLenth(self, nums):
        total_sum = 0
        index_map = dict()
        index_map[0] = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 0: #遇到0，减1
                total_sum -=1
            else:
                total_sum +=1
            if total_sum in index_map:
                res = max(res,i-index_map[total_sum])
            else:
                index_map[total_sum] = i
        return res
    
#前缀和 map:{cur, pos}
    
