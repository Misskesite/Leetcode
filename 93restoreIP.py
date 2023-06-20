# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:43:10 2019

@author: liuga
"""
#回溯
class Solution(object):
    def restoreIP(self, s):
        res = []
        self.dfs(s,0, "", res)
        return res
    
    def dfs(self, s, idx, path, res):
        if idx > 4:
            return 
        if idx == 4 and not s:
            res.append(path[:-1])
            return 
        for i in range(1, len(s)+1):
            if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                self.dfs(s[i:], idx+1, path+s[:i]+".", res)
            
#简易版?
class Solution(object):
    def restoreIP(self, s):
        if len(s) > 12:
            return []
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return

        for i in range(1, 4):
            if i > len(s):  #保证len(s) >= i 可以继续递归
                continue
            number = int(s[:i])
            if str(number) == s[:i] and number <= 255: #保证字符不是0X, 0XX
                self.dfs(s[i:], path +[s[:i]], res)
                    
            
class Solution2(object):
    def restoreIP(self, s):
        if len(s) < 4 or len(s)> 12:
            return []
        res = []
        def dfs(self, s, segment, ip):
             if segment == 4:
                if s == '':
                   res.append(ip[1:])  #去除最开始的.
                return
             for i in range(1,4):
                 if i <= len(s):
                     if int(s[:i]) <= 255:
                         self.dfs(s[i:], segment+1, ip +'.'+s[:i])
                         if s[0]=='0':
                             break
                     
         
         self.dfs(s, 0, res, '')
         return res

