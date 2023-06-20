# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:38:01 2019

@author: liuga
"""

class Solution(object):
    def plusOne(self, digits):
         carry = 1
         for i in range(len(digits)-1, -1, -1):
             digits[i]+= carry
             
             if digits[i] < 10: #某一位的数字没有产生进位，之后的高位也不可能进位了
                carry = 0
                break
             else:
                 digits[i] -=10                 
         if carry == 1:
             digits.insert(0,1)
                    
        return digits
             
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

