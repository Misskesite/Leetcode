# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:33:21 2020

@author: liuga
""" 
#right to left  F?1:T?4:5 -> F?1:(T?4:5) ->
class Solution(object):
    def parseTenary(self, expression):
        stack = []
        expr = list(expression)
        while len(stack) > 1 or expr:
            tail = stack[-5:]
            if len(tail)== 5 and tail[3] == "?" and tail[1] == ":":
                tail = tail[2] if tail[4] == "T" else tail[0]
                stack = stack[:-5] + [tail]
            else:
                stack.append(expr.pop())
        return stack[0] if stack else None
                
#时间复杂度O(n) 空间复杂度O(n)   从后向前遍历         
class Solution2(object):
    def parseRernary(self, expression):
        if not expression:
            return
        stack = []
        n = len(expression)
        for i in range(n-1, -1, -1): #right to left
            c = nums[i]
            if stack and stack[-1] == "?":
                stack.pop()
                first = stack.pop()
                stack.pop()
                second = stack.pop()

                if c == "T":
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(c)

        return stack[-1]
        
