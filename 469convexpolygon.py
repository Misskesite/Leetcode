# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:10:50 2020

@author: liuga
"""
# 判断相邻三个顶点A、B、C组成的两个向量(AB, AC)的叉积是否同负同正， 所有的顶点角都不大于180度
class Solution(object):
    def convexPolygon(self, points):
        
        def crossProduct(p0,p1,p2):
            x0,y0 = p0
            x1,y1 = p1
            x2,y2 = p2
            return (x2-x0)*(y2-y0) - (x1-x0)*(y2-y0)
        
        size = len(points)
        last = 0
        for x in range(size):
            p0,p1,p2 = points[x], points[(x+1)%size], points[(x+2)%size]
            p = crossProduct(p0,p1,p2) #这里需要判断是否为0，为0直接跳过
            if p*last < 0:
                return False
            last = p
        return True

#法向量的方向不变
class Solution2(object):
    def isConvex(self, points:List[List[int]]) -> bool:
        def calCrossProduct(A, B, C):
            AB = [B[0] - A[0], B[1] - A[1]]
            AC = [C[0] - A[0], C[1] - A[1]]
            return AB[0]*AC[1] - AB[1]*AC[0]

        falg = 0
        n = len(points)
        for i in range(n):
            #cur > 0说明points是按照逆时针输出的， cur<0说明按照顺时针
            cur = calCrossProduct(poitns[i], points[(i+1) % n], points[(i+2)% n)
            if cur != 0: #异号说明有个角度大于180度
                if cur.flag <0 : #跟之前的方向不同
                     return False
                else:
                     flag = cur
        return True
                                  
                                  
                                  
                                  
                                  
                                  
