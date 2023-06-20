# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:06:58 2020

@author: liuga
"""
#hashtable[val.first][val.second] = indexof(val)
#hashtable(val: [val.indices]) -> Array(val, index in hashtable)
# 2 : [2] -> {3, 0}
import random
import collections

class Solution(object):
    def _init_(self):
        self.mp = collections.defaultdict()
        self.output = []
        
    def insert(self,val):
        
        res = val not in self.mp
        self.mp[val].add(len(self.output))
        self.output.append(val) #末尾加入值
        return res              #len(mp[val]) == 1
    
    def remove(self,val):
        if val not in self.mp:
            return False
        last = self.output.pop()
        self.mp[last].remove(len(self.output))
        if val != last:         #删除的不是列表最后一个
            mp = self.mp[val].pop()
            self.mp[last].add(mp)
            self.output[mp] = last
        if not self.mp[val]:
            del self.mp[val]
        return True
    
    def getrandom(self):
         return self.output[random.randint(0, len(self.output)-1)]



class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.d = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        if val in self.d and len(self.d[val]) > 0:
            res = False
        else:
            res = True
        self.nums.append(val)
        # store element positions
        self.d[val].add(len(self.nums)-1)
        return res
        

    def remove(self, val: int) -> bool:
        if val in self.d and len(self.d[val]) > 0:
            pos = self.d[val].pop() # element to remove position            
            lpos = len(self.nums)-1 # last position
            lval = self.nums[lpos] # last val
            
            # add lval pos first .. then remove .. so when last == val .. it will take care auto
            self.d[lval].add(pos)            
            self.d[lval].remove(lpos)
            
            # swap with last
            self.nums[pos], self.nums[lpos] = self.nums[lpos], self.nums[pos]                        
            
            # remove element
            self.nums.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        size = len(self.nums)
        i = int(random.random()*size)
        return self.nums[i]
        




class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 字典，key 为值，value 为值对应的索引
        self.mp = collections.defaultdict(set)
        self.elements = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        # 添加索引到该值对应的索引中
        self.mp[val].add(len(self.elements))
        # 添加元素
        self.elements.append(val)
        # 示例中，如果元素已经在集合中，需要返回 False，这里判断下
        return len(self.mp[val]) == 1
        


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        # 删除元素，先判断元素是否存在
        if not self.mp[val]:
            return False
        # 否则，待删除元素与集合末尾元素进行交换
        # 元素可能重复，取元素其中一个对应的索引
        i = self.mp[val].pop()
        # 这里直接用末尾元素替换
        self.elements[i] = self.elements[-1]
        # 这里要注意，末尾元素集合对应的索引已经改变，要注意移除，添加新的索引
        last_num = self.elements.pop()
        # 弹出 last_num 后，这里 self.elements 元素数量减 1
        self.mp[last_num].discard(len(self.elements))
        #
        if i < len(self.elements):
            self.mp[last_num].add(i)
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.elements)
