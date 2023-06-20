# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:59:39 2020

@author: liuga
"""
#此法为主
class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0]*(len(nums)+1)
        self.nums = nums
        
        for i in range(len(nums)):
            self.add(i+1, nums[i])
    

    def add(self, i, val):
        while i <= len(self.nums):
            self.sums[i] += val
            i += i&-i # lowbit

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.sums[i]
            i -= i&-i
        return s

    def update(self, index: int, val: int) -> None:
        self.add(index+1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if not self.nums:
            return 0
        return self.sum(right+1) - self.sum(left)
    

#方法2
class  FenwickTree(object):
    def _init_(self, n):
        self._sums = [0 for _ in range(n+1)]

    def update(self, i, delta):
        while i < len(self._sums):
            self._sums[i] += delta
            i += i&-1

    def query(self, i):
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= i&-i
        return s

class NumArray:
    def _init_(self, nums):
        self._nums = nums
        self._tree = FenwickTree(len(nums))
        for i in range(len(nums)):
            self._tree.udpate(i+1, nums[i]) #数从1计数,所以+1

    def update(self, i, val):
        self._tree.update(i+1, val - self._nums[i])
        self._nums[i] = val

    def sumRange(self, i, j):
        return self._tree.query(j+1) - self._tree.query(i)
