# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:04:36 2020

@author: liuga
"""
#push() 时间复杂度是 O(1)；peek()/pop() 均摊时间复杂度是 O(1),空间复杂度 O(n)
class Solution(object):
    def _init_(self):
        #in负责push，out负责pop
        self.instack = []
        self.outstack = []
        
    def push(self,x):
        #新元素向in里面push
        self.instack.append(x)
    
    def pop(self):        
        if self.outstack:
            return self.outstack.pop()
        else:
            while self.instack:
                self.outstack.append(self.instack.pop())
            return self.outstack.pop()
            
            
    
    def peek(self):
        if self.outstack:
            return self.outstack[-1]:
        else:
            while self.instack:
                self.outstack.append(self.instack.pop())
            return self.outstack[-1]
                
    
    def empty(self):
        return not self.instack and not self.outstack
