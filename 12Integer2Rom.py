# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:52:07 2019

@author: liuga
"""

class Solution(object):
    def intToRoman(self, num):
        hashmap = {400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

        res = ''
        for key in hashmap:
            if num//key != 0:
                count = num//key          #输入4000 count为4
                res += hashmap[key]*count #count为hashmap中key的个数
                num %= key
        return res
                
