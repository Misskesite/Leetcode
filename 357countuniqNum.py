# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:59:40 2020

@author: liuga
"""
#输入2，输出91 (除去11 22 33 44 55 66 77 88 99)
class Solution(object):
    def countnumber(self, n):
        nums = [9,9,8,7,6,5,4,3,2,1] # [9,] + list(range(9, 0, -1))
        ans, product = 1,1
        for i in range(min(n,10)):
            product *= nums[i]
            ans += product
        return ans


'''
n = 0, 只有0，res = 1
n = 1, 有0, 1-9，res = 1+9 = 10
n = 2  10+ 9*9
n = 3, res(2) + 9*9*8
2 <= n <= 8 时，最高位不能选0 C(9,1) 后面的位数不能重复，每次减少一个数为A(9, n-i)
结果为 res = 1 + SUM(9* A(9, n-i))  1 <= i <= n
'''
#以此解为主
    def countnumber(self, n):
        if n == 0:
            return 1
        res = 10
        for i in range(1, n): #i=1 从十位数算起
            base = 9
            j = 9
            for k in range(i):
                base *= j
                j -= 1

            res += base
        return res
        
        
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res

