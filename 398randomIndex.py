# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:24:17 2020

@author: liuga
"""
import random

class Solution(object):
    def randomIndex(self, nums, k):
        
        e = nums.count(k)
        i = random.randint(1, e)
        for j in range(len(nums)):
            if nums[j] == k:
                i = i-1
                if i == 0:
                    return j


def __init__(self, nums):
    self.nums = nums
    
def pick(self, target):
    res = None
    count = 0
    for i, x in enumerate(self.nums):
        if x == target:
            count += 1
            chance = random.randint(1, count)
            if chance == count:
                res = i
    return res
