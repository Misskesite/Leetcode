# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:45:02 2019

@author: liuga
"""

class Solution(object):
    def intersectionTwoLS(self, headA, headB):
        lenA = lenB = 0
        p1 = headA
        p2 = headB
        
        while p1:
            p1 = p1.next
            lenA +=1
            
        while p2:
            p2 = p2.next
            lenB +=1
            
        if lenA > lenB:
            for i in range(lenA -lenB):
                headA = headA.next
        else:
            for i in range(lenB -lenA):
                headB = headB.next
                
        while headA and headB:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
            
            
        return None
    

class Solution2(object):
    def intersectionTwoLS(self, headA, headB):
        h1 = headA
        h2 = headB
        
        while h1 != h2:
            if not h1:
                h1 = headB
            else:
                h1 = h1.next
            
            if not h2:
                h2 = headA
            else:
                h2 = h2.next
                
        return h1
