# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:16:29 2019

@author: liuga
"""
         
class Solution3(object):
      def addTwoNumbers(self, l1, l2):     

      dummy = ListNode(0)
      pre = dummy
      carry = 0
      while l1 or l2 or carry :
            if l1:
                carry += l1.value
            if l2:
                carry += l2.value
            tmp = ListNode(carry % 10) #如果最高进位为1，添加节点
            pre.next = tmp
            pre = pre.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
            carry /=10
      return dummy.next
      
            
        
