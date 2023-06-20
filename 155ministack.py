# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:37:39 2019

@author: liuga
"""
#用辅助栈，存获取stack中的最小值，保证min_stack栈顶始终是最小元素
#min_stack等价于遍历stack中的所有元素，把升序的数字都删除，留下一个从栈底到栈顶的降序的栈
class MinStack(object):
    def _init_(self):
        self.stack = []
        self.minstack = []
    
    def push(self,x):
        self.stack.append(x)
        
        if not self.minstack :
            self.minstack.append(x)
        else:
            if x <= self.minstack[-1]:
                self.minstack.append(x)
            
    def pop(self):
        if self.stack:
            #等于的时候再出栈
            if self.minstack[-1] == self.stack[-1]:
                self.minstack.pop()
            self.stack.pop()
            
            
    def top(self):
        if self.stack:
            return self.stack[-1]
        
    def getmin(self):
        if self.minstack:
            return self.minstack[-1]
                


class MinStack:

    def __init__(self):
        self.stack = []
        self.m = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.m:
            self.m.append(val)
        else:
            self.m.append(min(self.m[-1], val))
        

    def pop(self) -> None:
        if self.m:
            self.m.pop()
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.m[-1]
