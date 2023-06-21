# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:27:54 2020

@author: liuga
"""
#汉明距离: 二进制位对应位不同的个数 4(0010) 14(1110) 2(0010)
class Solution(object):
    def hammingDistance(self, nums):
        res = 0
        for pos in range(32): #正数最大32位置
            bitcnt = 0
            for i in range(len(nums)):
                bitcnt += (nums[i] >> pos)&1 #每个位置 1找0的个数？
            res += bitcnt*(len(nums)-bitcnt)
        return res
    
计算每列的位置0和1的个数
4:     0 1 0 0

14:   1 1 1 0

2:     0 0 1 0

1:     0 0 0 1
