# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:24:59 2019

@author: liuga
"""
class ListNode(object):
    def _init_(self, x):
        self.val = x
        self.next= None

class Solution(object):
    def merge2Sortedarray(self, l1, l2):
        temp = ListNode(-1)
        head = temp
        
        while l1 and l2:
            if l1.val > l2.val:
                temp.next = l2
                l2 = l2.next
                
            else:
                temp.next = l1
                l1 = l1.next
            temp = temp.next
            
        if l1:
            temp.next = l1
        else:
            temp.next = l2
            
        return head.next
            
