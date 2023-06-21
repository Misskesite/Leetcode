# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:25:57 2020

@author: liuga
"""
#类似于31
#当数字是逆序时，已经是最大的数，因此找到逆序部分是关键
#找到逆序左侧的第一个数的下标i，找到逆序数组比下标i的数大的第一个数的下标j，将逆序数组反转，保证这部分值最小
class Solution(object):
    def nextGreatelemnt(self, num):
        s = list(str(num))
        i = len(s)- 2
        
        while i >= 0 and s[i] >= s[i + 1]:
            i -= 1
            
        if i < 0:
            return -1 #数字全部是逆序的，已经是最大值
        
        j = len(s) -1
        while s[j] <= s[i]:
            j -= 1
            
        s[i],s[j] = s[j], s[i]
        
        s[i+1:] = s[i+1:][::-1] #保证这部分值最小
        res = int(''.join(s))
        
        if res <= 2**31 -1:
            return res
        return -1
    
        
''''
对于 [2, 6, 3, 5, 4, 1] output  [2, 6, 4, 1, 3, 5]

先从后往前找到一个逆序数 i, 即为 3

然后再从 N 后面找到一个比它大的 "最小数"

即在 [5, 4, 1] 中找到比 3 大的最小数, 为 4

（这里可以直接再次从后往前找，因为这段数字倒着遍历必然是正序的）

交换两者位置，则为 [2, 6, 4, 5, 3, 1]

然后对一开始 N 后面位置进行反转

即从 [2, 6, 4, 5, 3, 1] 到 [2, 6, 4, 1, 3, 5]
