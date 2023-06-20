# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:13:56 2019

@author: liuga
"""
#栈 操作符位于操作数后面，也叫后缀表示法，语法树的后续遍历
#tokens = ["2","1","+","3","*"]  转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
#在python中，(-1)/2 = -1，而在c语言中，(-1)/2=0。也就是c语言中，除法是向零取整，即舍弃小数点后的数。而在python中，是向下取整的
class Solution(object):
    def evaluateRPN(self, tokens):
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
        
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:  #(int(first/second))
                    if first*second < 0:
                        stack.append(-((abs(first) // abs(second))))
                    else:
                        stack.append(first // second)
        
        return stack[0]
