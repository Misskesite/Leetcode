# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 17:27:26 2019

@author: liuga
"""

class Solution(object):
    def containduplicate(self, nums):
        mp = {}
        for n in nums:
            if n in mp:
                return True
            mp[n] = True
        return False
                
