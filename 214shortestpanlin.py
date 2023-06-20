# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:06:46 2019

@author: liuga
"""
#O(N) 拼接后将前缀后缀最大重复部分合并，next[j]表示j之前的字符串的最长前缀和后缀相等的字符个数，即最长前缀的下一个字符下标
class Solution(object):
    def shortestpanlin(self,s):
        n = len(s)
        if n == 0:
            return ""
        t = s[::-1]
        for i in range(n, 0, -1):
            if s[:i] == t[n-i:]:
                break
        return s[:i][::-1] + s
    
#haystack = "hello", needle = "ll"
#haystack = "aaaaa", needle = "bba"
#部分匹配值"就是"前缀"和"后缀"的最长的共有元素的长度 KMP匹配算法的复杂度O(m+n)
class Solution(object):
    def computer_next(pattern):
        nxt = [0]*(len(pattern) + 1)
        nxt[0] = -1
        nxt[1] = 0  #长度为1的没有前后缀
        i = 2
        k = 0        #指针指向pattern的位置
        while i < len(nxt):
            #当前字符匹配成功
            if pattern[i-1] == pattern[k]: #pattern索引比next索引小1
                nxt[i] = k+1
                k = next[i]
                i += 1
            #指针指向pattern[0] 却没有匹配成功
            elif k == 0:
                nxt[i] = 0
                i += 1
            else:
                k = nxt[k]  #利用已经匹配成功的信息，让指针不回退，查找next数组
        return nxt
        
#The only purpose of '*' is to reset the length of matched prefix.
class Solution:

    def shortestPalindrome(self, g):
        s = g + "|" + g[::-1]
        nxt = [-1] + [0] * len(s)
        l, r = -1, 0
        while r < len(s):
            while l >= 0 and s[l] != s[r]:
                l = nxt[l]
            l = l + 1 #相等 + 1
            r = r + 1
            nxt[r] = l
        return g[nxt[-1]:][::-1] + g

#此解法为主
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        '''KMP模板'''
        def prefix_function(s):     
            n = len(s)
            pi = [0] * n

            j = 0
            for i in range(1, n):
                while j>0 and s[i] != s[j]:     # 当前位置s[i]与s[j]不等
                    j = pi[j-1]                 # j指向之前位置，s[i]与s[j]继续比较

                if s[i] == s[j]:                # s[i]与s[j]相等，j+1，指向后一位
                    j += 1
                
                pi[i] = j
            return pi
        

        '''主程序''' special character to avoid overlap
        pi = prefix_function(s+'#'+s[::-1])     # s+'#'+s[n-1,...,0]的前缀函数
        if pi[-1] == len(s):                    # 前缀函数的最后一位即为s的最长回文前缀的长度
            return s
        else:
            return s[pi[-1]:][::-1] + s

#KMP算法 O(n)
#针对搜索词，算出一张《部分匹配表》(Partial Match Table) 移动位数 = 已匹配的字符数 - 对应的部分匹配值
#前缀(除了最后一个元素外，字符串的全部的头部组合)和后缀(除了第一个元素，字符串的全部尾部组合)的最长的共同元素的长度
class Solution(object):
    def shortestPanlindrome(self, s):
        def getPrefix(pattern):
            prefix = [-1]*len(pattern):
            j = -1

            for i in range(1, len(pattern)):
                while j > -1 ad pattern[j+1] != pattern[i]:
                    j = prefix[j] #向前回溯
                if pattern[j+1] == pattern[i]:
                    j += 1        #找到相同的前后缀
                prefix[i] = j
            return prefix

        if not s:
            return s

        #计算s的最长公共前后缀的长度
        A = s + s[::-1]
        prefix = getPrefix[A]
        i = prefix[-1]

        while i >= len(s):
            i = prefix[i]

        return s[i+1:][::-1] + s
            
                
'''
s和其转置r连接起来，中间加上一个其他字符，形成一个新的字符串t，还需要一个和t长度相同的一位数组 next，其中 next[i] 表示从 t[i] 到开头的子串的相同前缀后缀的个数
