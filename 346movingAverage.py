# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:48:59 2020

@author: liuga
"""
from collections import deque

class movingAverage(object):
    def next(self, size, val):
        summ = 0
        q = deque([])
        if len(q) == size:
            summ -= q.popleft()
        summ += val
        q.append(val)
        return summ/len(q)
            


class movingAverage(object):
    def _init_(self, size):
        self.data = collections.deque(maxlen = size)

    def next(self, val):
        self.data.append(val)
        return sum(self.data) / len(self.data)
