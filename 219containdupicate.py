# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:15:59 2019

@author: liuga
"""
#字典
class Solution(object):
    def containduplicate(self, nums, k):
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                if i - dic[n] <= k:
                    return True
            dic[n]  = i
        return False
    
                    
            
