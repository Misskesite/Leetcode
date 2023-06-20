# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:23:50 2020

@author: liuga
"""
#时间复杂度O(n) 空间复杂度O(1)
class Solution(object):
    def oddevenList(self, head):
        odd = ListNode(0)
        even = ListNode(0)
        oddHead, evenHead = odd, even
        index = 0  #isOdd = True
        while head:
            if index & 1 == 0: #if isOdd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            index += 1          #isOdd = not isOdd
        even.next = None
        odd.next = evenHead.next
        return oddHead.next
                
