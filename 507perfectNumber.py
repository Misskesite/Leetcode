# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:54:44 2020

@author: liuga
"""
#一个数是它之外的所有正因子之和相等
import math

class Solution(object):
    def perfectNumber(self, num):
         if num <= 1:
             return False
         sums = 1
         for i in range(2, int(math.sqrt(num))+1):
             if num % i == 0:
                 sums += i + num/i
         return num == sums
     
