# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:24:14 2020

@author: liuga
"""
#单调栈 维护 Leftmin [3 1 4 2] True 有个子模式[1 4 2] （i < j < k 和 nums[i] < nums[k] < nums[j]）
class Solution(object):
    def findPattern(self, nums):
        if len(nums) <= 2:
            return False
        
        third = float('-inf')
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < third:          # new value less than 3 value. then get 132 pattern
                return True
            else:
                while stack and stack[-1] < nums[i]:
                    third = stack.pop()  # have 32 mode
            stack.append(nums[i])
        return False


#遍历到一个位置 i 需要寻找数组中左边或者右边的所有数字和 nums[i] 的大小关系的题目，可以考虑一下单调栈
#时间复杂度O(n) 空间复杂度O(n)
class Solution2(object):
    def find132Pattern(self, nums):
        n = len(nums)
        leftMin = [float("inf")]*n

        for i in range(1, n):
            leftMin[i] = min(leftMin[i-1], nums[i-1])

        stack = []

        for j in range(n-1, -1, -1):
            numk = float("-inf")
            while stack and stack[-1] < nums[j]:
                numk = stack.pop()     #栈顶最小的元素？

            if leftMin[j] < numk:
                return True
            stack.append(nums[j])
        return False

'''
The 3 is always the maximum from right. It is clear.
The 2 is a maximum number which in 3's left. => This part is O(N)
But If we use stack, we can optimize this part to O(1)
