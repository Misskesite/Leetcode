# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:27:00 2020

@author: liuga
"""
#predix sum + binary search
'''
权重为 [1, 3]，表示有两个点，权重分别为1和3，那么就是说一个点的出现概率是四分之一，另一个出现的概率是四分之三。由于我们的rand()函数是等概率的随机
4个点，然后随机等概率取一个点，随机到第一个点后就表示原来的第一个点，随机到后三个点就表示原来的第二个点，这样就可以保证有权重的随机啦
randomly picks an index in proportion to its weight.
'''
import random

class Solution(object):
    def _init_(self,w):
        self.presum = [0]*len(w)
        self.presum[0] = w[0]
        for i in range(1,len(w)):
            self.presum[i] = self.presum[i-1]+ w[i]
            
    def pickIndex(self):        
        target = randint(0, self.presum[-1] - 1)
        l = 0
        r = len(self.presum) 

        while l < r: #搜索区间[l,r) 终止条件l == r
            m = (l + r) // 2
            if self.prefix[m] > target: #类似于bisect_right？ 疑问 下面的范围从1开始 用bisect_left，算小于等于随机数的下标？
                r = m
            else:
                l = m + 1

        return l
    
        
        
               
class Solution2(object):
    def _init_(self, w):
        self.pre = list(accumulate(w))
        self.total = sum(w)

    def pickIndex(self):
        x = random.randint(1, self.total)
        return bisect_left(self.pre, x)


''''
pre[i] - w[i] + 1 <= x <= pre[i] 找到第一个大于随机数的元素下标

若权重数组为 [1, 3, 2] 的话，那么累加和数组为 [1, 4, 6]，整个的权重和为6，我们 rand() % 6，
可以随机出范围 [0, 5] 内的数，随机到 0 则为第一个点，随机到 1，2，3 则为第二个点，随机到 4，5 则为第三个点，所以我们随机出一个数字x后，
然后再累加和数组中查找第一个大于随机数x的数字，使用二分查找法可以找到第一个大于随机数x的数字的坐标，
