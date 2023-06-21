# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:47:45 2020

@author: liuga
"""

import random

class Solution(object):
    def _init_(self, rects):
        self.rects = rects
        self.weights = []
        for [x_bl,y_bl,x_tr,y_tr] in self.rects:
            self.weights.append((x_tr-x_bl+1)*(y_tr-y_bl+1)) 
        
    def pick(self):
        [x_bl, y_bl, x_tr, y_tr] = random.choices(self.rects, weights=self.weights)[0]
        res = [random.randrange(x_bl, x_tr + 1), random.randrange(y_bl, y_tr + 1)]
        return res

#528的扩展
class Solution:
    def __init__(self, rects):
        w = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        self.weights = [i/sum(w) for i in accumulate(w)]
        self.rects = rects

    def pick(self):
        n_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n_rect] 
        return [random.randint(x1, x2),random.randint(y1, y2)] #等价于 ranrange(y1, y2+1)



class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = list(itertools.accumulate(
        [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]))

    def pick(self) -> List[int]:
        index = bisect_right(self.areas, randint(0, self.areas[-1] - 1))
        x1, y1, x2, y2 = self.rects[index]
        return [randint(x1, x2), randint(y1, y2)]

#此解法为主
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.sum = [0]
        for a, b, x, y in rects:
            self.sum.append(self.sum[-1] + (x - a + 1) * (y - b + 1))

    def pick(self) -> List[int]:
        k = randrange(self.sum[-1])
        rectIndex = bisect_right(self.sum, k) - 1
        x1, y1, x2, y2 = self.rects[index]
        return [randint(x1, x2), randint(y1, y2)]

