# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:18:24 2019

@author: liuga
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def myPrint(self):
         print(self.value)
         if self.next:
            self.next.myprint()
         
class Solution(object):
      def removeNnode(self, head, n):
          if not head:
              return head
          
          dummy = ListNode(-1)
          dummy.next = head
          prev = dummy
          cur = dummy
          while prev and n >=0:
              prev = prev.next
              n -= 1
          #如果列表长度等于n，prev到了末尾， cur不需要移动
          while prev: #prev走到末尾，cur刚好走到删除点
              prev = prev.next
              cur = cur.next
              
          cur.next = cur.next.next          
          return dummy.next



class Solution2(object):
    def removeNnode(self, head, n):
      

        lenth = 0
        cur = head
        while cur:
            lenth += 1
            cur = cur.next

        if n >= lenth:
            return head.next

        shift = lenth - n

        tmp = head
       
        while shift > 1:
            shift -= 1
            tmp = tmp.next
           
        tmp.next = tmp.next.next
        return head

        
        
