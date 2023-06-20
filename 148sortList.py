# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:32:50 2019

@author: liuga
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
#归并排序 时间复杂度 O(nlogn)  空间复杂度O(logn) 递归用到了栈     
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next  
        slow.next = None #断开2个链表
        
        l1 = self.sortList(head)
        l2 = self.sortList(mid)
        
        return self.mergeTwolists(l1, l2)
    
    def mergeTwolists(self, l1, l2):
        dummy = ListNode(0)
        node = dummy
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 if l1 else l2
        return dummy.next
