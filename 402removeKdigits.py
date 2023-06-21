# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:16:33 2020

@author: liuga
"""
# Create Maximum Number 
class Solution(object):
    def removeKdigits(self, num, k):
        if len(num) == k:
            return '0'
        stack  = []
        for n in num:
            while stack and k and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            stack.append(n)
        
        while k:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        
        return str(int("".join(stack))) #通过int去除前面的0？
             
#单调栈，移除数字，剩下的数最小 num = "1432219", k = 3. 输出 1219
class Solution2(object):
    def removeKdigits(self, num, k):
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit: #有可能删除的数<k 个
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'
    #数字序列为空，返回0。 删除前导0  num = "10200", k = 1 输出200

'''
栈顶元素在高位上，就算后面的数字再大，也是在低位上，我们只有将高位上的数字尽可能的变小
，才能使整个剩下的数字尽可能的小。这里虽然利用了单调栈的思想
