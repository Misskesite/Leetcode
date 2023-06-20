# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:19:05 2020

@author: liuga
"""

class PhoneDirectory(object):
    def  _init_(self, nums):
        self.list = [0 for _ in range(nums)]
        
    def get(self):
        for i, x in enumerate(self.list):
            if x == 0:
                self.list[i] == 1
                return i
        return -1

    def check(self, number):        
        return self.list[number] == 0
    
    def release(self, number):
        self.list[number] = 0
        
        
    
'''
用queue和set?
'''

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.maxnums = maxNumbers
        self.nums = deque()
        for n in range(self.maxnums):
            self.nums.append(n)
        self.count = Counter(self.nums)

    def get(self) -> int:
        if self.nums:
            num = self.nums.popleft()
            self.count[num] -= 1
            return num
        else:
            return -1

    def check(self, number: int) -> bool:
        if number in self.count and self.count[number] > 0:
            return True
        return False

    def release(self, number: int) -> None:
        if number not in self.count or self.count[number] == 0:
            self.nums.append(number)
            self.count[number] += 1		
