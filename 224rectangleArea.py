# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:50:41 2020

@author: liuga
"""

class Solution(object):
    def rectangle(self,A,B,C,D,E,F,G,H):
        points = [((A,B),(C,D)),((E,F),(G,H))]
        points.sort()
        ((A, B), (C, D)), ((E, F), (G, H)) = points
        area1 = (D-B)*(C-A)
        area2 = (H-F)*(G-E)
        x, y = (min(C, G) - max(A, E)), (min(D, H) - max(B, F))
        area = 0
        if x > 0  and y > 0:
            area = x*y
        return area1 + area2 - area

#不排序直接求
class Solution(object):
    def rectangle(self, ax1, ax2, ay1, ay2, bx1, bx2, by1, by2):
        #求两个矩形x轴相交的长度
        x = max(0, min(ax2, bx2) - max(ax1, bx1)) # if min(ax2, bx2) > max(ax1, bx1): x = min(ax2, bx2) > max(ax1, bx1) else 0
        #y轴相交的长度
        y = max(0, min(ay2, by2) - max(ay1, by1))
        #两个矩形面积 - 相交的面积
        return (ay2- ay1)*(ax2- ax1) + (by2- by1)*(bx2- bx1) - (x*y) #减去重合的

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        left = max(ax1,bx1)
        right = max(min(ax2, bx2), left)
        bottom = max(ay1,by1)
        top = max(min(by2, ay2), bottom)

        return (ax2 - ax1) * (ay2 - ay1) - (right - left) * (top - bottom) + (bx2 - bx1) * (by2 - by1)
