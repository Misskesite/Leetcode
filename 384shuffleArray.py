# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:17:01 2020

@author: liuga
"""
import random

class Solution(object):
    def _init_(self, nums):
        self.nums = nums
        
    def reset(self):
        return self.nums
    
    def shuffle(self):
        nums_s = self.nums[:]
        random.shuffle(nums_s)
        return nums_s


#洗牌算法
class Solution2:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy() #类似nums[:]

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j = random.randrange(i, len(self.nums))  #[i,n]之间随机抽取一个数
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

#Time O(n)
class Solution:
    def __init__(self, nums):
        self.nums = nums[:]
        self.copy = nums[:]

    def reset(self):
        self.nums = self.copy[:]
        return self.nums
        
    def shuffle(self):
        n = len(self.nums)
        for i in range(n):
            j = randint(i, n - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
