# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:12:02 2019

@author: liuga
"""

class Solution(object):
    def singleNum(self, nums):
        res = 0
        for i in range(32):
            cnt = 0
            mask = 1 << i
            for num in nums:
                if num & mask:
                    cnt += 1
            if cnt % 3 == 1:
                res |= mask
        if res >= 2 ** 31:
            res -= 2 ** 32
        return res
            
class Solution:
    def singleNumber(self, nums):
        single = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1<<i) == (1<<i):
                    count += 1
            single |= (count%3) << i
            
        return single if single < (1<<31) else single - (1<<32)   
