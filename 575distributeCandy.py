# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:19:21 2020

@author: liuga
"""
#贪心算法？
class Solution(object):
    def distributeCandies(self,candies):
        
        return min(len(set(candies)), len(candies)//2)
    
