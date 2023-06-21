# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:38:11 2020

@author: liuga
"""
# L >= W 而且W，L的差距比较小
import math

class Solution(object):
    def rectangle(self, area):
        sqrt = int(math.sqrt(area))
        for w in range(sqrt,0,-1): #能整除说明是正方形，不能的话，减1
            if area % w == 0:
                return [area // w, w] #地板除法
        return [area,1]
    
        
