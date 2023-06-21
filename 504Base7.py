# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:51:13 2020

@author: liuga
"""

class Solution(object):
    def base7(self, num):
        if num == 0:
            return "0"
        res = []
        sign = (num >= 0)
        num = abs(num)
        while num != 0:
            res.append(num%7)
            num //=7
        return ("" if sign else "-") + "".join(map(str,res[::-1]))
    #改写
        if sign:
            return "".join(res[::-1])
        else:
            return "-" + "".join(res[::-1])
    
            
            
        
            
        
# Recursive Solution       
     def convertToBase7(self, n):
        if n < 0:
            return '-' + self.convertToBase7(-n)
        if n < 7:
            return str(n)
        return self.convertToBase7(n // 7) + str(n % 7)

#Iterative Solution
    def convertToBase7(self, num):
        n, res = abs(num), ''
        while n:
            res = str(n % 7) + res
            n /= 7
        return '-' * (num < 0) + res or "0"
