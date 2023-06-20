# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:04:16 2019

@author: liuga
"""
#算出每一层的heighs传给84题的函数 单调栈，出栈得到前后边界，寻找边界，对每一个高度，遍历从左和向右的边界，对每个高度求一次面积
class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        n = len(matrix[0])
        
        result = 0
        heights = [0 for _ in range(n+1)] #后面加0？
        
        for row in matrix:
            for i in range(n):
                if row[i] == "1":
                    heights[i] = heights[i] + 1
                else:
                    heights[i] = 0
                    
            stack = [-1]
            for i in range(n+1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] -1
                    result = max(result, h*w)
                stack.append(i)
        return result
                
            
                
