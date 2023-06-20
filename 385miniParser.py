# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:43:40 2020

@author: liuga
"""

class Solution(object):
    def deserialize(self, s):
        
        def getnumber(nums):
            if isinstance(nums, int):
                return NestedInteger(nums)
            lst = NestedInteger()
            for num in nums:
                lst.add(getNumber(num))
            return lst
        return getNumber(eval(s))


#左至右遍历 s，如果遇到‘[’，则表示是一个新的NestedInteger 实例，需要将其入栈。
#如果遇到‘]’ 或 ‘,’，则表示是一个数字或者 NestedInteger 实例的结束，需要将其添加入栈顶的NestedInteger 实例。最后需返回栈顶的实例
#栈
class Solution2(object):
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack, num, last = [], "", ""
        for c in s:
            if c.isdigit() or c == "-": 
                num += c
            elif c == "," and num:
                stack[-1].add(NestedInteger(int(num)))#压入最后的一个嵌套list(nested list) 中 向栈顶添加值
                num = ""
            elif c == "[":
                elem = NestedInteger()
                
                stack.append(elem)
            elif c == "]": #结束
                if num:
                    stack[-1].add(NestedInteger(int(num))) 
                    num = ""
                if len(stack)> 1:
                    last = stack.pop() 
                    stack[-1].add(last) 
        return stack[-1]
'''
Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.

遇到 -0123456789 将连续的数字字符串取出， 并保留为 num
遇到 , 创建数值型的 NestedInteger 实例值为 num 并压入最后的一个嵌套 list 中
遇到 [ 创建一个嵌套类型的 NestedInteger list 实例值并压入栈中，并添加数值型的 NestedInteger 实例值为 None
遇到 ] 创建数值型的 NestedInteger 实例值为 num 并压入最后一个嵌套 list 中，并从栈中取出当前与 [ 匹配的list NestedInteger 实例
'''
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        stack, num, last = [], "", ""
        for c in s:
            if c.isdigit() or c == "-": 
                num += c
            elif c == "," and num:
                stack[-1].add(NestedInteger(int(num)))#压入最后的一个嵌套list(nested list) 中 向栈顶添加值
                num = ""
            elif c == "[":
                elem = NestedInteger()
                if stack: 
                    stack[-1].add(elem)
                stack.append(elem)
            elif c == "]": #结束
                if num:
                    stack[-1].add(NestedInteger(int(num))) 
                    num = ""
                last = stack.pop()  
        return last if last else NestedInteger(int(num))



#递归
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        index = 0

        def dfs() -> NestedInteger:
            nonlocal index
            if s[index] == '[':
                index += 1
                ni = NestedInteger()
                while s[index] != ']':
                    ni.add(dfs())
                    if s[index] == ',':
                        index += 1
                index += 1
                return ni
            else:
                negative = False
                if s[index] == '-':
                    negative = True
                    index += 1
                num = 0
                while index < len(s) and s[index].isdigit():
                    num *= 10
                    num += int(s[index])
                    index += 1
                if negative:
                    num = -num
                return NestedInteger(num)

        return dfs()
