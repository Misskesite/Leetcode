# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:15:43 2019

@author: liuga
"""

class Solution(object):
    def factorial(self,n):
        res = 0
        i = 5
        while n >= i:
            res += n/i
            i *= 5
            
        return res

#五步往上迭代
class Solution2(object):
    def trailingZero(self, n):
        zero_cnt = 0
        for i in range(5, n+1, 5):
            current = i
            while current %5 == 0:
                zero_cnt += 1
                current //= 5

        return zero_cnt

#检查5的幂，即检查i是否可以被5，25，125 整除
class Solution(object):
    def trailingZero(self, n):
        zero_cnt = 0
        for i in range(5, n+1, 5):
            power = 5
            while i % power == 0:
                zero_cnt += 1
                power *= 5

        return zero_cnt
            
