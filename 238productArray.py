# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:32:53 2020

@author: liuga
"""


#前缀和版本
class Solution2(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        r1, r2, ans = [1]*n, [1]*n, [1]*n

        for i in range(1, n):
            r1[i] = r1[i-1]* nums[i-1]

        for i in range(n-2 , -1, -1):
            r2[i] = r2[i+1]* nums[i+1]

        for i in range(n):
            ans[i] = r1[i]* r2[i]

        return ans
    

#对上面的空间优化
class Solution2(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1]*n

        ans[0] = 1
        for i in range(1, n): #左边数字的乘积
            ans[i] = ans[i-1]* nums[i-1]
            
        right = 1
        for i in range(n-1, -1, -1):
            ans[i] = ans[i]*right
            right *= nums[i]       #只跟前一个值有关，用k代替
        return ans

    
