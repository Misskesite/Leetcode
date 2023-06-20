# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:42:52 2019

@author: liuga
"""
#时间复杂度O(n) 空间复杂度O(1) 先保留前两个，然后依次从后面跟第一个，然后第二个对比
class Solution(object):
    def removeDupicate2(self,nums):
        count = 0
        for i in range(len(nums)):
            if count < 2 or nums[count-2] != nums[i]:
                nums[count] = nums[i]
                count += 1
                
        return count
            


class Solution(object):
    def removeDuplicate(nums):
        n = len(nums)
        if n <= 2:
            return n

        slow = 2
        fast = 2
        while fast < n:
            if nums[slow -2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1
        return slow
