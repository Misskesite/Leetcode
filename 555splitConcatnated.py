# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:54:01 2020

@author: liuga
"""
#每个字符串可以逆序或者不变，将字符串按照原始顺序拼接组成一个字符串,求字典序最大的字符串
class Solution(object):
    def splitConcatnated(self, strs):
        
        strs = [max(s, s[::-1]) for s in strs]
        ans  = ''
        for i, st in enumerate(strs):
            left = ''.join(strs[:i])     #被分割的字符串之前的字符串
            right  = ''.join(strs[i+1:]) #被分割的字符串后面的字符串
            for s in (st, st[::-1]):
                for j in range(len(s)): #遍历每一个位置？
                    ans = max(ans, s[j:] + right +  left + s[:j])
        return ans

'''
四种情况分别分割，暴力法
abc xyz
abc zyx
cba xyz
cba zyx

每个字符串找字典序最大，cut位置的字母一定是最大的那个
zyx cba
先从z
