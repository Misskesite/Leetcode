# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:36:58 2019

@author: liuga
"""
from collections import deque

class impleteStack(object):
    def _init_(self):
        self.que = deque()
    
    def pop(self):
        if self.queue:
            return self.que.popleft()
    
    def push(self, x):
        self.que.append(x)
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
           
    
    def top(self):
        return self.que[0] #队列最左边
    
    def empty(self):
        return not self.que
            
        
        
