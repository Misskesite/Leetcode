# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:30:07 2019

@author: liuga
"""

class ListNode(object):
    def _init_(self, x):
        self.val = x
        self.next = None
        
#时间复杂度O(n), 空间复杂度O(1)   
class Solution(object):
    def removeDuplicate(self, head):
        dummy = ListNode(0)
        dummy.next = head
        
        cur = dummy
                
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
                
            else:
                cur = cur.next
                    
        return dummy.next
            
                 
class Solution2(object):
    def removeDuplicate2(self, head):
        if head == None or head.next == None:
            return head
        
        dummy = ListNode(0, head)
        pre = dummy
        
        
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
                
            if pre.next == head:
                pre = pre.next
                    
            else:
                pre.next = head.next
                    
            head = head.next
            
        return dummy.next


def deleteDuplicates(self, head):
    dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next
