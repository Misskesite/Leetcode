# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:41:49 2019

@author: liuga
"""
#时间复杂度O(n),需要遍历字符串一次。空间复杂度O(n)，取决于栈的空间，栈的个数不超过n
#思路是把所有的* /先计算出来，最后计算只有 +, - 运算符的表达式。数字1, 运算符2, 数字3
#数字1 栈中保存为栈顶元素,数字2为 pre_op, 数字3用num保存。如果运算符是+，-则把数字3(取反)入栈
#* /则需要计算，把结果入栈   时间复杂度O(n), 空间复杂度O(n) 5+3*4-40/8-9
class Solution(object):
    def calculator(self, s):
        stack = []
        pre_op = "+"
        num = 0
        for i, each in enumerate(s):
            if each == " ":
                continue #错误，如果结尾为空，i == n - 1 没法入栈计算
            if each.isdigit():
                num = num*10 + int(each)
            if i == len(s)-1 or each in '+-*/':
                if pre_op == "+": #上一个运算符
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                elif pre_op == "*":
                    stack.append(stack.pop()*num)
                elif pre_op == "/":                    
                    stack.append(int(stack.pop() / num)) 
                    
                pre_op = each
                num = 0
        return sum(stack)

#此法为主
 def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        preOp = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit(): #换成 if s[i].isdigit()：也可以
                num = num * 10 + int(s[i])
            if i == n - 1 or s[i] in '+-*/':
                if preOp == '+':
                    stack.append(num)
                elif preOp == '-':
                    stack.append(-num)
                elif preOp == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                preOp = s[i]
                num = 0
        return sum(stack)
    

#向0取整，负数时向上取整，正数时向下取整。正负数python中可用int(x)取整数部分实现， int(2.3) = 2 int(-2.3) = -2 反斜杠//能实现向下取整 1//5 = 0 -1//5 = -1
#3+2*2 = 7   3+5/2 = 5  10-3/2 = 9
class Solution2:
    def calculate(self, s):
        if not s:
            return '0'
        stack, cur, op = [], 0, '+'
        for c in s + '+':
            if c == " ":
                continue
            elif c.isdigit():
                cur = (cur * 10) + int(c)
            else:
                if op == '-':
                    stack.append(-cur)
                elif op == '+':
                    stack.append(cur)
                elif op == '*':
                    stack.append(stack.pop() * cur)
                elif op == '/':
                    stack.append(int(stack.pop() / cur))
                cur, op = 0, c
        return sum(stack)
