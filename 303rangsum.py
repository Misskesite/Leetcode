# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:08:25 2020

@author: liuga
"""

class Solution(object):
    def rangeSum(self, nums, i, j):
        n = len(nums)
        sums = [0]*(n+1)
        for i in range(1,n+1):
            sums[i] = sums[i-1]+ nums[i-1]
        return sums[j+1] - sums[i]

'''
前缀和原理
pre_sum[i] = nums[0] + ... + nums[i]
nums[i] = pre_sum[i] - pre_sum[i-1]
nums[l] + ... + nums[r] = pre_sum[r] - pre_sum[l-1]
由于题目中设置pre_sum[0] = 0 所有index往后+1
所以
nums[l] + ... + num[r] = pre_sum[r+1] - pre_sum[l]
