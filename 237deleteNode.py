# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:19:38 2020

@author: liuga
"""
#没有给出头节点，先赋值，再删除节点。时间复杂度O(1),空间复杂度O(1)
class Solution(object):
    def deleteNode(self, node): #原地删除
        node.val = node.next.val
        node.next = node.next.next
        
