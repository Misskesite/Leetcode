# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:38:00 2020

@author: liuga
"""
#理解递归,类似于第2题目?
class Solution(object):
    def plusOne(head):
        if not head:
            return head
        
        def dfs(node):
            if not node:
                return 1
            carry = dfs(node.next)
            sum = node.val + carry
            node.val = sum %10
            return sum/10
            
        carry = dfs(head)
        if carry == 1:
            res = ListNode(1)
            res.next = head
            return res
        return head
    
#此解法为主
class Solution2(object):
    def plusOne(self, head):
        l = []
        while head:
            l.append(head)
            head = head.next

        i = len(l) -1
        while i >= 0 :
            l[i].val += 1
            if l[i].val >= 10:
                l[i].val -= 10
                i -= 1
            else:
                break

        if i == -1: #最左边有进位
            root = ListNode(1)
            root.next = l[0]
            return root
         else:
             return l[0]
            


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        
        while  head:
            if head.val != 9:
                cur = head  #point to the rightmost non-9 node
            head = head.next
    
        cur.val += 1
        while cur.next:
            cur.next.val = 0
            cur = cur.next

        if dummy.val == 0:
            return dummy.next 
        else:
            return dummy
