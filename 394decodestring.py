# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:36:13 2020

@author: liuga
"""

class Solution(object):
    def decodeString(self, s):
        curnum = 0
        curstring = ''
        stack  = []
        for char in s:
            if char == "[":
                stack.append(curstring)
                stack.append(curnum)
                curstring = ''
                curnum = 0
            elif char == ']':
                prenum = stack.pop()
                prestring = stack.pop()
                curstring = prestring + prenum*curstring
            elif char.isdigit():
                curnum = curnum*10 + int(char)
            else:
                curstring += char
        return curstring
                
                
#栈实现 [之前的字符串进栈操作，清空，遇到]出栈操作，计算
#s = "3[a2[c]]", return "accaccacc".
class Solution(object):
    def decodeString(self, s):
        stack = []
        curstr = ""
        num = 0
        for c in s:
            if c == '[':
                stack.append([num, curstr]) #(左括号前的字符串, 左括号前的数字)
                curstr, num = "", 0
            elif c == ']':
                pre_num, pre_str = stack.pop()
                curstr = pre_str + pre_num*curstr

            elif '0' <= c <= '9' : #c.isdigit()
                num = num*10 + int(c)

            else:
                curstr += c
        return curstr
                
                                              
                                              
            
