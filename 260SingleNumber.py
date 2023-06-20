# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:32:32 2020

@author: liuga
"""
import collections
#O(n) O(n)
class Solution(object):
    def SingleNUmber(self, nums):
        lookup = collections.defaultdict(int)
        for num in nums:
            lookup[num] += 1
        res = []
        
        for k, v in lookup.items():
            if v == 1:
                res.append(k)
        return res
                
        
#位运算时间复杂度O(n) 空间复杂度O(1)
class Solution(object):
    def singleNumber(self, nums):
        xorSum = 0         # = x1^x2
        for num in nums:
            xorSum ^= num

        lsb = xorSum &(-xorSum) 
        type1 = type2 = 0  #x1, x2出现在不用类
        for num in nums:
            if num & lsb:  #两类: 二进制第l位为1的数，和l位为0的数
                type1 ^= num
            else:
                type2 ^= num
        return [type1, type2]
                

        
