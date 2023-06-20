# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:57:57 2019

@author: liuga
"""
#左括号("(", "[" ,"{")直接入栈，否则右括号，而且栈不为空，如果是右括号，栈弹出来的不是左括号，返回false
class Solution(object):
    def validParenthesis(self, s):
        if len(s) %2 == 1:
            return False
            
        stack = []
        left = ("(", "[" ,"{")
        right = (")", "]", "}")
        zip(left, right)
        for v in s:
            if v in left:
                stack.append(v)
            else:
                if not stack: #栈为空，还来了个右括号，返回false
                    return False
                p = stack.pop()
                if left.index(p) != right.index(v):
                    return False
        return len(stack) == 0


class Solution2(object):
    def validParenthesis(self, s):
        dic = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
            else:
                stack.append(i)
        return not stack



