# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:54:43 2020

@author: liuga
"""
#此解法为主
class Solution:
    def __init__(self):
        self.dic = {}

    def encode(self, s: str) -> str:
        if s in self.dic:
            return self.dic[s]
        i = (s+s).find(s,1)
        if i < len(s):
            encoded = str(len(s)//i) + '[' + self.encode(s[:i]) + ']'  
            if len(encoded) < len(s):      
                self.dic[s] = encoded
                return encoded
           
        encoded = s
        splitEncoded = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1,len(s))]
        shortest = min(splitEncoded + [encoded] ,key = len)
        self.dic[s] = shortest
        return shortest
'''
For any s, you can either

Do not encode it
Or encode it to one string if possible
Or, split it into two, encode the two substring to their shortest possible length, and combine them

choose the shortest result from 1~3.
During this process, we should use dic to record the best encoding result for all substrings, so that it can be reused.
'''

    
class Solution(object):
    def _init_(self):
        self.dp = dict()
        
    def encodeString(self, s):
        size = len(s)
        if size <= 1:
            return s
        if s in self.dp:
            return self.dp[s]
        ans = s
        for p in range(1,size+1):
            left = s[:p]
            right = s[p:]
            t = self.solve(left)+ self.encode(right)
            if len(t) < len(ans):
                ans = t
        self.dp[s] = ans
        return ans
    
    def solve(self,s):
        ans = s
        size = len(s)
        for x in range(1, size/2+1):
            if size % x or s[:x]*(size/x) != s:
                continue
            y = str(size/x) + '[' + self.encode(s[:x]) + ']'
            if len(y) < len(ans):
                ans = y
        return ans
            
#自顶向下
#abbbabbbcabbbabbbc -> 2[2[abbb]c]  aabcaabcd -> 2[aabc]d  aaaaa -> 5a
        
import functools
class Solution2:
    @functools.lru_cache(None)
    def encode(self, s):
        res = s
        for i in range(1, len(s)+1):
            tmp = s[:i]
            res = min(res, tmp + self.encode(s[i:]), key = len)
            cnt = 1
            j = i
            while s[j:].find(tmp) == 0:
                cnt += 1
                j += len(tmp)
                res = min(res, str(cnt)) + "[" + self.encode(tmp) + "]" + self.encode(s[j:], key = len)
        return res


#动态规划DP[i][j] 表示在[i,j]范围内字符串的缩写形式 时间复杂度O(n**3) 空间复杂度O(n**2)
class Solution(object):
    def encode(self, s):
        n = len(s)
        for step in range(1, n + 1):
            for i in range(n + 1 - step):
                j = i + step -1
                dp[i][j] = s[i:j]
                for k in range(i, j):
                    left = dp[i][k]
                    right = dp[k+1][j]
                    if len(left) + len(right) < len(dp[i][j]):
                        dp[i][j] = left + right

                t = s[i: j]
                replace = ""
                pos = (t + t).find(t,1)#从index为1的字符开始搜索  abababab，搜索的位置为2
                if pos >= len(t):
                    replace = t
                else:
                    replace = str(len(t)/pos) + '[' + dp[i][i + pos -1] + ']'

                if len(replace) < len(dp[i][j]):
                    dp[i][j] = replace

        return dp[0][n-1]
                

    
