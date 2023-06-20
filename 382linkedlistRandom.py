# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:05:52 2020

@author: liuga
"""
#时间空间复杂度O(n)
import random
class Solution(object):
    def _init_(self, head):
        
        self.stack = []
        while head:
            self.stack.append(head.val)
            head = head.next
    
    def getRandom(self):
        l = len(self.stack)
        return self.stack[random.randint(0, l-1)]

#时间复杂度O(n) 空间复杂度O(1) 随机生成数，遍历到表
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.root = head

    def getRandom(self) -> int:
        node, ans, i = self.root, None, 0
        while node:
            if not randint(0, i): #随机数为0
                ans = node.val
            node, i = node.next, i + 1
        return ans

''''
从前往后处理每个样本，每个样本成为答案的概率为1/i
其中 i为样本编号（编号从 1开始），最终可以确保每个样本成为答案的概率均为 1/n （其中 n为样本总数）

