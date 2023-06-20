# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:41:15 2019

@author: liuga
"""

class Solution(object):
    def multiplyString(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        len1 = len(num1)
        len2 = len(num2)
        
        temp = [0 for _ in range(len1+len2)]
        # Do multiply 把数字倒过来
        for i in range(len1):
            for j in range(len2):
                temp[i+j] += int(num1[i]) * int(num2[j])
        carry = 0
        digits = []
        
        #do plus
        for num in temp:
            s = carry + num
            carry = s//10
            digits.append(str(s%10))
        result = "".join(digits)[::-1]
        
        # Remove the surplus zero
        sub_index = 0
        for i in range(len1 + len2 -1):
            if result[i] == "0":
                sub_index += 1
            else:
                break
        result = result[sub_index:]
        return result
                
                
def multiply(self, num1: str, num2: str) -> str:
    s = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            mult = int(num1[i]) * int(num2[j])
            summ = mult + s[i + j + 1]
            s[i + j] += summ // 10
            s[i + j + 1] = summ % 10

    for i, c in enumerate(s):
        if c != 0:
            break

    return ''.join(map(str, s[i:]))         
