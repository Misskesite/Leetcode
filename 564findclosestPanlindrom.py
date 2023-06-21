# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:36:40 2020

@author: liuga
"""
#低位修改会带来高位的修改，尽量修改靠近中间的位置
class Solution(object):
    def findclosestPanlindrom(self, n):
        evenPal = lambda sp: int(sp + sp[::-1])
        oddPal = lambda sp: int(sp + sp[::-1][1:])
        sn, n = n, int(n)
        if len(sn) == 1:
            return str(n-1)
        ans = -999999999999
        mid = len(sn)/2
        for sp in sn[:mid], sn[:mid+1], str(int(sn[:mid])):
            p = int(sp)
            for pal in evenPal, oddPal:
                for d in -1, 0, 1:
                    val = pal(str(p+d))
                    if val == n:
                        continue
                    ans = min(ans,val, key =  lambda x : (abs(x-n), x))
                    
        return str(ans)
                    

#本身是回文，比如121 可以变成 111 131分别堆中间的2进行了 -1， +1， +0操作(要考虑是否引起长度改变比如99->100)
#不是回文123，变成121，只需要改变右半边。 取出包括中间数的左半边，比如123就取出12，1234也取出12，然后就要根据左半边生成右半边
class Solution2(object):
    def nearestPalindromic(self, n):
        if int(n) < 10:
            return str(int(n)-1)

        if int(n) <= 11:
            return '9'

        #get the first half
        mid = len(n)//2
        halfnum = int(n[:-mid])

        #prepare the 3 candidates
        nums = [0]*3

        for i in [-1, 0, 1]:
            nums[i+1] = str(halfnum + i)
            nums[i+1] += nums[i+1][:mid][::-1]
            nums[i+1] = int(nums[i+1])

        #cover the case like 1000
        if len(str(nums[0])) + 2 == len(n):
            nums[0] = nums[0]*10 + 9

        #cover the case when diff[1] == n
        diff = [abs(num)- int(n) for num in nums]
        if diff[1] == 0:
            diff[1] = float("inf")

        ind = diff.index(min(diff))
        return str(nums[ind])
        


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m, l = len(n), int(n)

        # 0-9 和 10^m 次幂的全部按照 n-1 获得回文串 e.g 100
        if l < 10 or l == 10 ** (m-1):
            return str(l-1)

        # 10^m - 1 次幂的全部按照 n+2 获得回文串    e.g 99
        if l == 10 ** m - 1: 
            return str(l + 2)

        # 10^(m-1) + 1 次幂的全部按照 n-2 获得回文串 e.g 101
        if l == 10 ** (m-1) + 1: 
            return str(l - 2)

        # 其他数据用折半法获取回文字符串
        min_num = float('+inf')
        palid_num_str = '0'
        pre_int = int(n[:(m+1)//2]) # 加一折半，避免分奇偶数

        # 最近的回文只可能为前缀整数的±1
        for dx in (-1, 0, 1):
            palid_pre = str(pre_int + dx)   #e.g. 123
            palid_num = int(palid_pre[:m//2] + palid_pre[::-1])

            diff = abs(palid_num - l)
            if diff > 0 and min_num > diff:
                palid_num_str = str(palid_num)
                min_num = diff
        return palid_num_str
