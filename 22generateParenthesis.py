# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:27:19 2019

@author: liuga
"""
#减法 left左括号可以使用的个数, right是右括号可以使用的个数
#可以只在序列仍然保持有效时才添加‘(’ 或 ‘)’
class Solution(object):
    def generateParenthesis(self,n):
        
        result = []
        self.dfs(n, n, "", result)
        return result
    
    def dfs(self, left, right, path, result):
        if left == 0 and right == 0:
            result.append(path)
            return
        
        if left > 0:
            self.dfs(left - 1, right, path + "(", result)
            
        if right > left: #右括号剩余的比左括号多
            self.dfs(left, right - 1, path + ")", result)            
    
#加法 , 保证当前形成的字符串左括号数量大于等于右括号数量，剪枝 if left > n or right > left, return 
class Solutions(object):
    def generateParenthesis(self, n):
        path = ""
        res = []
        left = right = 0   
        def backtrack(path, left, right, n):
            if left == n and right == n:
                res.append(path)
                return
            
            if left < right: #剪枝 会出现‘)(‘ 这样的非法串
                return
            
            if left < n:
                backtrack(path + "(", left+1, right, n)
                
            if right < n: #可以修改为left > right，已经填的左括号比较多
                backtrack(path + ")", left, right+1, n)
        
        backtrack(path, 0, 0, n)
        return res

#上面方法的改写
def generateParenthesis(self, n):
    res = []
    if n <= 0:
        return res

    def dfs(path, left, right):
        if left > n or right > n or right > left: #剪枝 
            return
        if len(path) == 2 * n: #left == n and right == n:
            res.append(path)
            return

        dfs(path + "(", left + 1, right)
        dfs(path + ")", left, right + 1)

    dfs("", 0, 0)
    return res
