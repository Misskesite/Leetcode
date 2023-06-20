# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:37:04 2020

@author: liuga
"""
#位运算 对整数 a,b 不考虑进位，无进位的加法 a异或b 需要进位为a&b ，进位后的结果(a&b)<<1
class Solution(object):
    def sunofTwo(self, a, b):
        MASK = 0x10000000
        while b !=0 :
            carry = a & b
            a = (a ^ b) % MASK
            b = (carry << 1) % MASK
        if a < 0x7fffffff :
            return a
        else:
            return a|(~0x100000000 +1)


MASK1 = 4294967296  # 2^32
MASK2 = 2147483648  # 2^31
MASK3 = 2147483647  # 2^31-1

class Solution:
    def getSum(self, a: int, b: int) -> int:
        a %= MASK1
        b %= MASK1
        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = carry
        if a & MASK2:  # 负数
            return ~((a ^ MASK2) ^ MASK3)
        else:  # 正数
            return a

'''' -1在计算机里就全是1 oxFFFFFF
正数的反码与原码相同，负数的反码为原码除符号位意外各位取反
正数的补码跟原码相同，负数的补码为原码符号位以外的所有位取反加1
可以将减法转化为补码的加法运算。
''''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        ## RC ##
        ## APPROACH : BITWISE OPERATIONS ##
        ## LOGIC ##
        #   1. For any two numbers, if their binary representations are completely opposite, then XOR operation will directly produce sum of numbers ( in this case carry is 0 )
        #   2. what if the numbers binary representation is not completely opposite, XOR will only have part of the sum and remaining will be carry, which can be produced by and operation followed by left shift operation.
        #   3. For Example 18, 13 => 10010, 01101 => XOR => 11101 => 31 (ans found), and operation => carry => 0
        #   4. For Example 7, 5
        #   1 1 1                   1 1 1
        #   1 0 1                   1 0 1
        #   -----                   -----
        #   0 1 0   => XOR => 2     1 0 1  => carry => after left shift => 1 0 1 0
        #   2                                                              10
        # now we have to find sum of 2, 10 i.e a is replace with XOR result and b is replaced wth carry result
        # similarly repeating this process till carry is 0
        #   steps will be 7|5 => 2|10 => 8|4  => 12|0
        
		## TIME COMPLEXITY : O(1) ##
		## SPACE COMPLEXITY : O(1) ##
        
        # 32 bit mask in hexadecimal
        mask = 0xffffffff # (python default int size is not 32bit, it is very large number, so to prevent overflow and stop running into infinite loop, we use 32bit mask to limit int size to 32bit )
        while(b & mask > 0):
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a
