# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:43:06 2020

@author: liuga
"""
import random

class RandomizedSet(object):
    def _init_(self):
        self.nums = list()
        self.dic = dict()
        
    def insert(self, val):
        if val not in self.dic:
            self.nums.append(val)
            self.dic[val] = len(self.nums)-1 #插入尾部，建立映射
            return True
        else:
            return False
        
    #删除任意索引需要线性时间，解决方法：删除最后一个元素。(将要删除的元素和最后一个元素交换)
    def remove(self, val):
        if val in self.dic:
            idx =  self.dic[val]
            last = self.nums[-1]
            
            self.nums[idx] = last
            self.dic[last] = idx
            
            self.nums.pop()
            self.dic.pop(val,0) #del self.dic[val]
            return True
        return False

    from random inport choice   
    def getrandom(self):
        idx = random.randint(0, len(self.nums)-1)
        return self.nums[idx]
        #return choice(self.nums)
