# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 22:22:43 2020

@author: liuga
"""

class Solution(object):
    def meetingrooms(self, v):
        if not intervals:
            return True
        v.sort(key = lambda val:val.start)
        for i in range(1,len(v)):
            if v[i].start < v[i-1].end:
                return False
        return True
    
