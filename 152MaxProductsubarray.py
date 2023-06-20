# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:51:34 2019

@author: liuga
"""
#时间空间复杂度O(n) 和nums[i]比较，特殊情况：之前的元素都是0  [2,3,-2,4]输出6
class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        n = len(nums)
        maxDP = [0]*n
        minDP = [0]*n
        maxDP[0] = minDP[0] = nums[0]

        #最大积的可能情况有：元素nums[i]，上一个最大积与nums[i]累乘，上一个最小积与nums[i]累乘
        for i in range(1, n):
            maxDP(i) = max(maxDP(i-1)*nums[i], nums[i], minDP(i-1)*nums[i])
            minDP(i) = min(minDP(i-1)*nums[i], nums[i], maxDP(i-1)*nums[i])
            
            res = max(res, maxDP(i))
            
        return res

#第i个状态和i-1个状态相关，根据滚动数组思想，用两个变量维护
class Solution2(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        n = len(nums)
        res = nums[0]

        maxF = nums[0]
        minF = nums[0]

        for i in range(1, n):
            ''' 需要加下面这段吗？
            if nums[i] == 0:
                maxF, minF = 1, 1
                continue        
            '''
            mx = maxF
            mn = minF
            maxF = max(mx*nums[i], nums[i],mn*nums[i])
            minF = min(mn*nums[i], nums[i],mx*nums[i])
            res = max(res, maxF)
        return res
        
