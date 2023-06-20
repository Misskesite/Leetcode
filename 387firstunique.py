# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 13:08:45 2020

@author: liuga
"""
#哈希表 字典
class Solution(object):
    def firstunique(self, nums):
         mp = {}
         for n in nums:
             if n in mp:
                 mp[n] = 1
             else:
                 mp[n] += 1
                 
         for i in range(len(nums)):
             if mp[nums[i]] == 1:
                 return i
         return -1
