# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:06:16 2019

@author: liuga
"""

class Solution(object):
    def hasCycle(self,head):
         slow = fast = head
         
         while fast and fast.next:
             slow = slow.next
             fast = fast.next.next
             if slow == fast:
                  return True
         return False