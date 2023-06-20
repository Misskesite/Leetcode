# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:35:49 2019

@author: liuga
"""
#添加一个虚拟头节点
class Solution(object):
    def removeElement(sefl,head,val):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
    
#leetcode 204
import math

class Solution2(object):
    def countPrimes(n):
        
        cnt = 0
        def judge_prime(w):
            squrt_w = int(math.sqrt(w))
            for i in range(2, squrt_w+1):
                if x%i == 0:
                    return 0
            return 1
        for x in range(2,n):
            cnt = cnt + judge_prime(x)
        
        return cnt
    
