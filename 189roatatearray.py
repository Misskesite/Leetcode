# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 17:38:48 2019

@author: liuga
"""
#冒号创立了新的切片，旧列表的值赋给新列表 时间复杂度O(n) 空间复杂度O(1) 因为没有用额外的空间
class Solution(object):
    def roatetArray(self,nums,k):
        k = k % (len(nums))
        nums[:] = nums[n-k:] + nums[:n-k]


#
    def roatetArray(self,nums,k):
        k = k % (len(nums))
        nums.reverse()
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))
