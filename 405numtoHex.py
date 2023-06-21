# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:04:28 2020

@author: liuga
"""
#正数和0的补码就是该数字本身再补上最高位元0。 负数的补码则是将其对应正数按位取反再加1
class Solution(object):
    def numtoHex(self, num):
         if num == 0:
             return '0'
         res = ""
         if num < 0:
             num += 1 << 32
         while num:
             last = num % 16
             if last < 10:
                 res = str(last) + res
             else:
                 res = chr(last -10 + ord('a')) +  res
             num /= 16
         return res


#输入26 输出1a  输入-1 输出ffffffff
CONV = "0123456789abcdef"
class Solution2:
    def toHex(self, num: int) -> str:
        ans = []
        # 32位2进制数，转换成16进制 -> 4个一组，一共八组
        for _ in range(8):
            ans.append(num%16)
            num //= 16 #负数取整，一直是-1
            if not num:
                break
        return "".join(CONV[n] for n in ans[::-1])


class Solution:
    def toHex(self, num: int) -> str:
        s = '0123456789abcdef'
        res = ''
        num = num & 0xFFFFFFFF
        while num:
            res += s[num % 16]
            num >>= 4
        
        return res[::-1] or '0'

'''
 if num < 0:
        cur = (-num ^ 0xffffffff) + 1
    else:
        cur = num
'''
