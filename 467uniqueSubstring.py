# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:24:54 2020

@author: liuga
"""
#求出以每个字符(a-z)为结束字符的最长连续字符串
#"zab" 输出6 1+2+3  满足题意的p的子字符串要么是单一的字符，要么是按字母顺序的子字符串
import collections

class Solution(object):
    def uniqueSubstring(self, p):
        
        count = collections.defaultdict(int)
        n = len(p)
        c = 0 #也可以初始化为1
        for i in range(n):
            if i > 0 and (ord(p[i]) - ord(p[i-1]) == 1 or (p[i]=='a' and p[i-1] == 'z')): #连续或者首尾(连续)
                c += 1
            else:
                c = 1 #i = 0
            count[p[i]] = max(count[p[i]], c) #字典去重复，比如cac, c会被计算2次, 比如bab, b的值计算2次不同
        return sum(count.values()) #所有值相加
    

#动态规划 26个字母出现的长度最大是多少 计所有a-z为结尾的最长字符串，求和就是答案 dp[i]记录以i位置为结尾的最长连续字符串长度，要么是1，要么是dp[i-1]+1
class Solution(object):
    def uniqueSubstring(self, p):
        n = len(nums)
        dp  = [0]*26
        
        count = 1
        for i in range(len(p)):
            if i > 0 and ord(p[i]) - ord(p[i-1]) == 1 or (p[i]=='a' and p[i-1] == 'z'):
                count += 1
            else:
                count = 1
            dp[ord(p[i]) - ord('a')] = max(dp[ord(p[i]) - ord('a')], count)

        res = 0
        for i in range(len(dp)):
            res += dp[i]
        return res
    
            
'''
数学方法
索引为 i 结尾的子数组个数就是 i + 1 这道题可以直接用等差数列求和公式 (1 + n) * n / 2，其中 n 数组长度(最长的substring)。
