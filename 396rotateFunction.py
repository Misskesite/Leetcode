# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:10:14 2020

@author: liuga
"""

class Solution(object):
    def rotatefunction(self, A):
        
        _sum = 0
        n = len(A)
        f = 0
        for i, a in enumerate(A):
            _sum += a
            f += i*a
        res = f
        for i in range(n-1, 0 , -1):
            f = f + _sum - n *A[i]
            res = max(res, f)
        return res


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f, n, numSum = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            f += i * num
        res = f
        for i in range(n - 1, 0, -1):
            f = f + numSum - n * nums[i]
            res = max(res, f)
        return res

'''
F(1) = F(0) + sum - nums[n-1]* len(nums); 
F(2) = F(1) + sum - nums[n-2]* len(nums)；

nums = [4,3,2,6]
F(1) = 0*6 + 1*4 + 2*3 + 3 *2
F(2) = 0*2 + 1*6 + 2*4 + 3 *3 = F(1) + sum - 4*2 (nums[-2])

