# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:51:01 2019

@author: liuga
"""

class Solution(object):
    def reverse(self,x):
         sign = 0
         if x < 0 :
             sign = -1
         else:
             sign = 1
         x *= sign
         result = 0
         
         while x:
             result = result*10 + x % 10
             x/=10
             
         if result > 2147483647:
             return 0
         else:
             return result*sign
             
        