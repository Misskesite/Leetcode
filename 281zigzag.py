# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:02:49 2020

@author: liuga
"""
#如果只有2个vector,可以两个指针来回切换2个数组，如果是k个，需要用queue来存，然后pop出来
class ZigzagIterator(object):
    def _init_(self, v1, v2):
        self.v = []
        i = 0 
        while i < max(len(v1), len(v2)):
            if i < len(v1):
                self.v.append(v1[i])
            if i < len(v2):
                self.v.append(v2[i])
            i += 1
        self.index = 0
        
    def next(self):
        cur = self.v[self.index]
        self.index += 1
        return cur
    
    def hasNext(self):
        if self.index < len(self.v):
            return True
        else:
            return False



#iter函数生成迭代器 iter(object)
#交叉依次返回元素值的iterator。轮流遍历=>依次插入对应数组的iterator进queue，每次next后抛出队首，如果iterator还有元素再插回队尾。
import collections
class ZigzagIterator(object):
    def _init_(self, v1, v2):
        self.q = collections.deque()         #加入2个迭代器?
        if len(v1) > 0:
            self.q.append((len(v1), iter(v1)))
        if len(v2) > 0:
            self.q.append((len(v2), iter(v2)))

        
    def next(self):
        l , it = self.q.popleft() #it为迭代器？

        if l > 1:     #iterator还有元素再插回队尾
            self.q.append((l - 1, it))
        return next(it) #next后抛出队首 next(iterable)函数

    def hasNext(self):
        return bool(self.q)

#此解法为主
#cur标识应该读取哪个deque，读取该deque的头部，修改变量cur
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.q1 = deque(v1)
        self.q2 = deque(v2)
        if len(v1):
            self.cur = 1
        else:
            self.cur = 0

    def next(self) -> int:
        val = 0
        if self.cur == 1:
            val = self.q1.popleft()
            if len(self.q2) != 0:
                self.cur = 0
        elif self.cur == 0:
            val = self.q2.popleft()
            if len(self.q1) != 0:
                self.cur = 1
        return val
        
    def hasNext(self) -> bool:
        return len(self.q1) != 0 or len(self.q2) != 0
    
#follow up, k个数组
#用一个 queue 里面保存 iterator 的 pair，在初始化的时候，有几个数组就生成几个 pair 放到 queue 中，每个 pair 保存该数组的首位置和尾位置的 iterator，在 next() 函数中，
#取出 queue 队首的一个 pair，如果当前的 iterator 不等于 end()，将其下一个位置的 iterator 和 end 存入队尾，然后返回当前位置的值
