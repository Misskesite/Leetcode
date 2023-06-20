# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:58:01 2020

@author: liuga
"""
# [0 1 0 3 12]  ->  [1 3 12 0 0] do it in-place without making copy of the aray
#j记录非零的个数，只要是非0的统统赋给nums[j]
class Solution(object):
    def movingZero(self, nums):
        j = 0
        for i in range(len(nums)):
            if num[i] != 0:
                nums[j] = nums[i]
                i += 1
                
        #剩下的都是0，把末尾的元素赋为0
        for i in range(j, len(nums)):
            nums[i] = 0
        

#快速排序思想，0当成中间点，不等于0的放在左边，等于0的放在右边，只要nums[i]!=0 交换nums[i]和nums[j]
class Solution2(object):
    def moveZeros(self, nums):
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

'''
nums = [0, 1, 0, 3, 12] 输出 [1, 3, 12, 0, 0]
