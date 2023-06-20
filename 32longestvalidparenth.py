# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:33:56 2019

@author: liuga
"""

class Solution(object):
    def longestValidparen(self,s):
        if not s:
            return 0
        length = len(s)
        dp = [0 for _ in range(length)]
        for i in range(1,length):
            if s[i] == ")":
    
             j = i- 1- dp[i-1]
             if j >=0 and s[j] == "(":
                 
                 dp[i] = dp[i-2] + 2
             
                 if j-1>=0 :
                     dp[i] +=dp[j-1]
             
        return max(dp)
    

    def checkParentheses(arr):
        if not arr:
            return 0
            
        maxlen = 0
        stack = []
        last = -1 #比如()
        for i in range(len(arr)):
            if arr[i]=='(':
                stack.append(i)     # push the INDEX into the stack
            else:
                if stack == []:
                    last = i  #因为(不入栈，做个标记
                    
                else:
                    stack.pop()
                    if stack == []:
                        maxlen = max(maxlen, i-last)
                        
                    else:
                        maxlen = max(maxlen, i-stack[-1]) #比如多余的(
                        
                        
        return maxlen
