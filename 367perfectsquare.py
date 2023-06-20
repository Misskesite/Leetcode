# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:09:43 2020

@author: liuga
"""

class Solution(object):
    def perfectSquare(self, num):
        l = 0
        r = num +1
        while l < r:
            mid = l + (r-l)/2
            if mid*mid == num:
                return True
            if mid*mid < num:
                l = mid+1
            else:
                r = mid
        return False
    
                
    def perfectSquare(self, num):
        l = 0
        r = num
        while l <= r:
            mid = l + (r-l)//2
            if mid*mid == num:
                return True
            if mid*mid < num:
                l = mid+1
            else:
                r = mid-1
        return False
