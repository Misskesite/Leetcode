# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:51:03 2019

@author: liuga
"""
#左右两侧最近的高度小于 h 的柱子(两边第一个小于它的值)
#单调栈 存放的元素具有单调性. 当元素出栈时，说明这个新元素是出栈元素向后找第一个比其小的元素
#元素出栈后，说明新栈顶元素是出栈元素向前找第一个比其小的元素
class Solution(object):
    def largestRectangle(self, heights):
        heights.append(0) #避免非空判断,如果是递增的话，无法弹出计算面积
        #加入哨兵结点，在循环中就不用做非空判断
        stack = [-1]
        result = 0
        
        N = len(heights)
        for i in range(N):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                
                w = i - stack[-1] -1
                result = max(result, h*w)
            stack.append(i)
        #heights.pop()
        return result


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0] #不加0，遍历完成后栈中还有元素
        res = 0
        for i in range(len(heights)):
            
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                res = max(res, (i - stack[-1] - 1) * h)
            stack.append(i)
        return res

