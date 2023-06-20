# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:54:06 2019

@author: liuga
"""
#回溯，原因是不是找到依次截取a,aa, aab,前缀是回文，继续产生分支。前缀不是回文，剪枝
class Solution(object):
    def partition(self,s):
        
        self.isPalindrome = lambda s : s == s[::-1]
        res = []               
        self.dfs(s, res, [])
        return res
    
    def dfs(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                self.dfs(s[i+1:], res, path + [s[:i+1]])
            
        
#回溯加记忆, 预处理之后，我们只需要 O(1)判断s[i..j] 是否为回文串了 时间复杂度O(n*2^n + n*n),长度为n的划分方案2^(n-1)
class Solution2(object):
    def partition(self, s):
        res = []
        n = len(s)
        dp = [[False]* n for _ in range(n)]
        for j in range(n):
            for i in range(j+1):
                if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
               

        def dfs(i, path):        
            if i == n:
                res.append(path)
                return
            for j in range(i, n):
                if dp[i][j] == True:
                    
                    dfs(j+1, path + [s[i:j+1]])                    
                    
        dfs(0, [])
        return res

