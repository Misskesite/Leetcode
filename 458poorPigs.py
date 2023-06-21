# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:03:45 2020

@author: liuga
"""
#贪心？ 输入：buckets = 1000, minutesToDie = 15, minutesToTest = 60，输出5
class Solution(object):
    def poorpigs(self, buckets, mintoDo, minTotest):
        test = mintoDo/minTotest +1
        pigs = 0
        while test ** pigs < buckets:
            pigs += 1
        return pigs
    
            
'''
如果是2只猪，喝混合水判断
