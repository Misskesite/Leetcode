# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:45:45 2020

@author: liuga
"""

import collections

class PerceftSquare(object):
    def isrectangle(self,rectangles):
        left = min(x[0] for x in rectangles)
        bottom = min(x[1] for x in rectangles)
        right = max(x[2] for x in rectangles)
        top = max(x[3] for x in rectangles)
        
        points = collections.defaultdict()
        for l,b,r,t in rectangles:
            A,B,C,D = (l,b), (r,b) (r,t), (l,t)
            for p,q in zip((A,B,C,D),(1,2,4,8)):
                if points[p]&q:
                    return False
                points[p] |= q
                
        for px, py in points:
            if left < px < right or bottom < py < top:
                if points[(px,py)] not in (3,6,9,12,15):
                    return False
        return True
    
                
#左下角，左上角，右下角，右上角一定是矩阵的最外圈，面积和与完美矩阵的面积
#任意不是这四个顶点的小矩阵的点，一定会出现两次或四次（如果出现四次以上，一定有超过四个矩阵以这个点为顶点，那么必然有重叠；如果出现奇数次，那么必然没有被完整覆盖）【这个的判断可以去掉面积相等，但是是内部重叠的情况】
class Solution:
    def isRectangleCover(self, rectangles):
        x, y, a, b, s = inf, inf, -inf, -inf, 0
        cnts = Counter()
        for x_, y_, a_, b_ in rectangles:
            x, y, a, b = min(x, x_), min(y, y_), max(a, a_), max(b, b_)
            s += (a_ - x_) * (b_ - y_)
            cnts[(x_, y_)] += 1
            cnts[(a_, b_)] += 1
            cnts[(x_, b_)] += 1
            cnts[(a_, y_)] += 1
        if s != (a - x) * (b - y):
            return False
        ps = {(x, y), (x, b), (a, y), (a, b)}
        for p in ps:
            if cnts[p] != 1: #最外角的点个数为1
                return False
        for i, v in cnts.items():
            if v > 4 or (i not in ps and v % 2): #不在边界的点不能是奇数次. v == 2 or v == 4
                return False
        '''
        for p in ps:
            del cnts[p]
        return all(c == 2 or c == 4 for c in cnts.values())

        '''
        return True


