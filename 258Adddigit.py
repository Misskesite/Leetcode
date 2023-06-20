# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:11:16 2020

@author: liuga
"""

class Solution(object):
    def adddigit(self, num):
        while num >= 10:
            tmp = 0 #表示sum
            while num :
                tmp += num %10
                num /= 10
            num = tmp
        return num
                
