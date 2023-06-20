# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:25:08 2019

@author: liuga
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
#时间复杂度O(n)
class Solution(object):
    def revrselinkedList(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        
        node = dummy
        for _ in range(m-1):
            node = node.next
            
        pre = node.next
        cur = pre.next
        
        for _ in range(n-m): #把列表逆向反转
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
            
        node.next.next = cur  #node.next 对应翻转后最左边的节点
        node.next = pre       #pre对应翻转后最右边的节点
        
        return dummy.next 
    
        
    
#头插法 O(n)迭代法 空间复杂度 O(1)
class Solution(object):
    def reverseBetween(self, head, m ,n):
        dummy = Node(-1)
        dummy.next = head
        pre = dummy

        for i in range(m-1):
            pre = pre.next

        cur = pre.next   #把nxt指向的元素依次移到逆向列表的最前面
        for i in range(n-m): 
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt

        return dummy.next
       
        
