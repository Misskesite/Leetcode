# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:40:38 2021

@author: liuga
"""
#157可以读一次， 158可以读好几次
class Solution(object):
    head = 0
    tail = 0
    buffer = ['']*4
    def read(self, buf, n):
        i = 0
        while i < n:
            if self.head == self.tail: #read4缓冲区为空
                self.head = 0
                self.tail = read4(self.buff) #开始进缓冲区
                if self.tail == 0:
                    break
            while i < n and self.head < self.tail:
                buf[i] = self.buffer[self.head]
                i += 1
                self.head += 1
        return i


#此解法为主
class Solution:
    def __init__(self):
        self.queue = collections.deque()

    def read(self, buf: List[str], n: int) -> int:
        
        i = 0
        while i < n:
            buf4 = [''] * 4 
            _ = read4(buf4) 
            self.queue.extend(buf4)
            count = min(len(self.queue), n-i) 
            if not count:
                break
            buf[i:] = [self.queue.popleft() for _ in range(count)]
            i += count
        return i
    
