# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:47:43 2020

@author: liuga
"""
#模为m的前i项和的最小下标
class Solution(object):
    def continuousSubarray(self, nums, k):
        dmap = {0: -1}
        prefix  = 0
        for i, n in enumerate(nums):
            prefix += n
            if k != 0:
                prefix %= k
            if prefix not in dmap: #不能整除
                dmap[prefix] = i
            elif dmap[prefix] + 1 < i: #能整除，距离大于2
                return True
        return False
    
#从开始到现在所有距离2以上的前缀和余数
#[i,j]的区间满足(presum[j] - presum[i]) % k == 0，那么显然要有presum[j] % k == presum[i] % k
class Solution(object):
    def checkSubarray(self, nums, k):
        modes = set()
        presum = 0
        for num in nums:
            last = presum
            #当前前缀和
            presum += num
            presum %= k
            #同余定理
            if presum in modes:
                return True
            #上一个前缀和，下一个就可以用了(距离为2)
            modes.add(last)
        return False
            
