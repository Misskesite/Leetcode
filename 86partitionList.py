# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:23:47 2019

@author: liuga
"""
class ListNode:
    def _init_(self,x):
        self.val = x
        self.next = None
        
class Solution(object):
    def partitionList(self, head, x):
        if not head or not head.next:
            return head
        
        p1 = small_dummy = ListNode(-1)
        p2 = large_dummy = ListNode(-1)
        p = head
        
        while p:            
            if p.val < x:
                p1.next = p
                p1= p1.next  #p1 = p 指针移位
            else:
                p2.next = p
                p2 = p2.next #p2 = p 指针移位
            p = p.next

        #最后将两个链表合起来即为答案   
        p1.next = large_dummy.next
        p2.next = None
        
        return small_dummy.next
        
