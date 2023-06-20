# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:04:36 2020

@author: liuga
"""

class Solution(object):
    def _init_(self):
        self.instack = []
        self.outstack = []
        
    def push(self,x):
        self.instack.append(x)
    
    def pop(self,x):
        self.peek()
        self.outstack.pop()
    
    def peek(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]
    
    def empty(self):
        return not self.instack and not self.outstack