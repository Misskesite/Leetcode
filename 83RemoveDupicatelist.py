# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:00:59 2019

@author: liuga
"""

class ListNode(object):
    def _init_(self, x):
        self.val = x
        self.next= None
    
class Solution(object):
    def removeDuplicate(self, head):
        curr = head
        while curr and cur.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
