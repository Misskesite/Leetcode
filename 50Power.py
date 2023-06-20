# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:57:30 2019

@author: liuga
"""
#返回值float 快速幂 + 迭代
class Solution(object):
    def multiply(self, x, n):
        sign = 1 if n >= 0 else -1
        result = 1.0
        n = abs(n)
        while n > 0:
            if n % 2 == 1:
                result *=x
            
            x *= x
            n //= 2
        if sign < 0:
            result = 1.0/result
        return result
                

#快速幂 + 递归
class Solution(object):
    def multiply(self, x, n):
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N//2)
            return y*y if N%2 == 0 else y*y*x

        return quickMul(n) if n >= 0 else 1.0/quickMul(-n)
