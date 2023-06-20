# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:05:50 2020

@author: liuga
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
[1,2,3,4,5,6]
"""



class Solution(object):
    def _init_(self, vec2d):
        self.vec = vec2d
        self.row = 0
        self.col = 0
        i = 0
        while self.row != len(self.vec):
            if len(self.vec[self.row]) != 0:
                self.col = 0
                break
            self.row +=1
            
    def next(self):
        ret = self.vec[self.row][self.col]
        self.col += 1
        return ret
        
    def hasNext(self):
        if self.row == len(self.vec):
            return False
        if self.col != len(self.vec[self.row]):
            return True
        else:
            self.row += 1
            while self.row != len(self.vec):
                if len(self.vec[self.row]) != 0:
                    self.col = 0
                    return True
                self.row +=1
        return False

#此解法为主
class Solution(object):
    def _init_(self, v):
        self.list = []
        for nums in v:
            for item in nums:
                self.list.append(item)
        self.index = 0

    def next(self):
        self.index += 1
        return self.list[self.index -1]

    def hasnext(self):
        return self.index != len(self.list)
    
        
