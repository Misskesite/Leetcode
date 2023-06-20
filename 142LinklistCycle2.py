# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:46:20 2019

@author: liuga
"""
#fast points move 2 times faster than slow points. f = 2s, f = s + nb(相遇时刚好多走了n圈) 第一次相遇slow指针走了nb步
class Solution(object):
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast


