# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:19:26 2019

@author: liuga
"""

class Solution(object):
    def firstMissingpositive(self, nums):
        if not nums:
            return 1
        i = 0
        length = len(nums)
        while i < length:
             current = nums[i]
             if current <=0 or current > length or current[i]==current[i-1]:
                 i+=1
                 
             else:
                 nums[current-1], nums[i] = nums[i], nums[current-1]
                 
             for i in range(length):
                 if nums[i] != i+1:
                     return i+1
                     
             return length+1

            
#时间复杂度O(n), 空间复杂度O(1)    哈希映射 数值为i的数映射到下标i-1的位置                
#3 让每个数字n都回到下标n-1的家里。3放在索引为2的地方， 4放在索引为3的地方
class Solution(object):
    def firstMissingPositive(self, nums):
        
        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]
            
        n = len(nums)
        #先判断这个数是不是索引。然后判断这个数是不是放在正确的地方 [3,4,-1,1] nums[2] ,nums[0] = nums[0], nums[2]
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1]  != nums[i]:
                swap(nums, nums[i]-1, i)

        #[1, -1, 3, 4]
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
                       
        #都正确，返回数组长度+1
        return n +1
        


    def firstMissingPositive(self, nums):
        n = len(nums)

        # Correct slot:
        # nums[i] = i + 1
        # nums[i] - 1 = i
        # nums[nums[i] - 1] = nums[i]
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1

        return n + 1
'''
# Correct slot:
# nums[i] = i + 1
# nums[i] - 1 = i
# nums[nums[i] - 1] = nums[i]
