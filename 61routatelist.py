# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:25:05 2019

@author: liuga
"""

class ListNode(object):
    def _init_(self,x):
        self.val = x
        self.next = None
        
class Solution(object):
    def rotateList(self, head, k):
        if not head:
            return []
        
        cur = head
        length = 1
        
        while cur.next:
            length += 1
            cur = cur.next
         
        cur.next = head  #头尾相连，闭合为环
       
        #向右移动k>=n时，我们仅需要移动k mod n次    
        shift = length - k % length
        
        #断开的位置倒数第k位置   
        for _ in range(shift):
            cur = cur.next
                
        result = cur.next
        cur.next = None   #新的头节点之前断开
        return result
            

class Solution:
  def rotateRight(self, head: ListNode, k: int) -> ListNode:
      if not head or not head.next or k == 0:
          return head

        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head  # circle the list

        t = length - k % length
        for _ in range(t):
            tail = tail.next
        newHead = tail.next
        tail.next = None

        return newHead
