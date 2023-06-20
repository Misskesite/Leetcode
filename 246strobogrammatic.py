# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 22:48:22 2020

@author: liuga
"""

class Solution(object):
    def isstrobogrammatic(self, num):
        d = {'0':'0', '1':'1','6':'9', '8':'8','9':'6'} #遗漏1
        ans = ""
        for n in num:
            if n not in d:
                return False
            ans += d[n]
        return ans[::-1] == num #反转与原字符对比
    
            
