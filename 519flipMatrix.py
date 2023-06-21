# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:04:17 2020

@author: liuga
"""
#类似于拒绝采样 可以用一个 HashSet 来记录翻转过了点，这样也方便进行查重操/
import random

class Solution(object):
    def __init__(self, n_rows, n_cols):
        self.num = n_rows * n_cols #转成一维的
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.lookup = {}

    def flip(self): #每次调用，翻过的点都是之前没有翻过的
        self.num -= 1
        i = random.randint(0, self.num)
        idx = self.lookup.get(i, i) #查找位置i对应的映射
        self.lookup[i] = self.lookup.get(self.num, self.num) #i和num(最后一个数字)映射？
        self.lookup[self.num] = idx
        return [idx // self.n_cols, idx % self.n_cols]

        
#矩阵中的位置 (i, j)，它对应了map 中的元素map[i×n+j]
    def reset(self):
        self.lookup.clear()
        self.num = self.n_cols * self.n_rows



class Solution:
    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total = m * n - 1
        self.record = dict()

    def flip(self) -> List[int]:
        r = random.randint(0, self.total)
        idx = self.record.get(r, r)
        # 相当于total的值没被用，将那个值填入idx位置；
        # 被用了的话，将它那里填入的没被用的值填入
        self.record[r] = self.record.get(self.total, self.total)
        self.total -= 1
        ans = [idx // self.n, idx % self.n]
        return ans

    def reset(self) -> None:
        self.total = self.m * self.n - 1
        self.record = dict()
