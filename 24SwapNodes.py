# -*- coding: utf-8 -*-
"""
Created on Fri Sep 2 21:15:55 2019

@author: liuga
"""

class listNode(object):
    def _init_(self,x):
        self.val =x
        self.next = None

#1->2->3->4 to 2->1->4->3 操作三步骤 pre.next = node2, node1.next = node2.next, node2.next = node1         
class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummy = listNode(0);
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            node1 = p.next
            node2 = p.next.next
            p.next = node2
            node1.next = node2.next
            node2.next = node1
            
            
            p = p.next.next
            
        return dummy.next
#改写
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummy = listNode(0);
        dummy.next = head

        pre = dummy
        cur = head

        while cur and cur.next:
            nxt = cur.next.next
            second = cur.next

            #reverse this pair
            second.next = cur
            cur.next = nxt
            prev.next = second

            #update ptr
            prev = cur
            cur = nxt
        return dummy.next
    

#Recursion
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

            
