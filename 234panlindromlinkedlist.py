# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 18:42:30 2020

@author: liuga
"""
#时间复杂度 O(n)
class Solution(object):
    def panlindrom(self,head):
        if not head or not head.next:
            return True
        list = []
        while head:
            res.append(head.val)
            head = head.next
        
        n = len(list)
        if list[i] != list[n-i-1]:
            return False
        return True


#快慢指针
class Solution2(object):
    def panlindrom(self,head):
        if not head or not head.next:
            return True
    slow, fast = head, head
    pre  =  None

    while fast and fast.next: #快指针走到末尾，慢指针走到中间，其中把前半部分反转
        
        fast = fast.next.next
        #反转
        next = slow.next
        slow.next = prev
        prev = slow
        slow = next

    if fast:
        slow = slow.next

    while pre and slow:
        if pre.val != slow.val:
            return False
        pre = pre.next
        slow = slow.next
        
    return True
