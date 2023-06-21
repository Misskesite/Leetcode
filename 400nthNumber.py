# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:41:07 2020

@author: liuga
"""

class Solution(object):
    def findNthdigit(self, n):
        cur = 1
        cnt = 9
        start  = 1
        while n > cur*cnt:
            n -= cur*cnt
            cur += 1
            cnt *= 10
            start *= 10
        start += (n-1)/cur
        return int(str(start)[(n-1) % cur]) #(n-1) % cur]为index

''''
1位数 9个   1*9
2位数 90个  2*90
3位数 900个 3*900

'''
# n = 200  200-9-180 = 11 转化为0开始的坐标就是10.那它就是三位数里面的 10//3 =3 即 103， 我们要找103的(10%3 = 1) 位就是0
class Solution:
    def findNthDigit(self, n: int) -> int:
        cur, base = 1, 9
        while n > cur * base:
            n -= cur * base
            cur += 1
            base *= 10
        n -= 1
        # 数字
        num = 10 ** (cur - 1) + n // cur
        # 数字里的第几位
        idx = n % cur
        return num // (10 ** (cur - 1 - idx)) % 10



class Solution:
    def findNthDigit(self, n: int) -> int:
        start, digits = 1, 1
        while n > 9 * start * digits:
            n -= 9 * start * digits
            start = 10 ** digits
            digits += 1
        
        return int(str(start + (n-1)//digits)[(n-1) % digits])
