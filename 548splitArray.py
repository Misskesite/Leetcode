# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:35:34 2019

@author: liuga
"""
#前缀和 加入set 空间换时间 固定j,前后i,k的位置变换
class Solution(object):
    def splitArray(self, nums):
        if len(nums) < 7: #4个和中间有间隔
            return False
        accum_sum = [0]*len(nums)
        accum_sum[0] = nums[0]

        n = len(nums)
        
        for i in range(1, n):
            accum_sum[i] = accum_sum[i-1] + nums[i]
        
        for j in range(3, n-3): #j > i+1 从3开始 j< n -3 j是中间的分割点
            lookup = set()
            for i in range(1, j-1):
                #sum(0,i-1)  sum(i+1, j-1)
                if accum_sum[i-1] == accum_sum[j-1]-accum_sum[i]:
                    lookup.add(accum_sum[i-1])
            for k in range(j+2, len(nums)-1):
                #sum3 = accum_sum[n-1]-accum_sum[k]  sum4 = accum_sum[k-1]-accum_sum[j]
                if accum_sum[n-1]-accum_sum[k] == accum_sum[k-1]-accum_sum[j] and accum_sum[k - 1] - accum_sum[j] in lookup:
                    return True
        return False
        
                    
                    
                    
        
