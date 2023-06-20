# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:36:47 2019

@author: liuga
"""

class Solution(object):
    def lengthLastword(self, s):
        return len(s.strip().split('')[-1])
    
        N = len(s)
        left, right = 0, N-1
        while right >=0 and s[right] == "":
             right -=1
             
             left = right
             
        while left>=0 and s[left] != "":
             left-=1
             
        return right - left
         
         

class Solution2(object):
    def lengthLastword(self, s):
        N = len(s)
        count = 0
        for i in range(N-1, -1, -1):
            if s[i] == " ":
                if count != 0:
                    break
            else:
                count += 1
                    
        return count
            
    
