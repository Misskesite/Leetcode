# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:30:19 2020

@author: liuga
"""

class Point(object):
    def _init_(self,a=0,b=0):
        self.x = a
        self.y = b
        
class Solution(object):
    def outerTree(self, points):
        n = len(points)
        if n <= 3:
            return points
        lb = min(points, key = lambda p:(p.y,p.x))
        ccw = lambda p1,p2,p3 : (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
        dsquare = lambda p1, p2: (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
        cmp = lambda p,q: ccw(1b,q,p) or dsquare(p,1b) - dsquare(q,1b)
        points.sort(cmp)
        
        x = n-1
        while x and ccw(lb, points[x], points[x - 1]) == 0: x -= 1:
            points = points[:x] + points[x:][::-1]
            stack = [points[0], points[1]]
        
        for x in range(2,n):
            while len(stack) >1 and ccw(stack[-2],stack[-1], points[x]) < 0:
                stack.pop()
                stack.append(points[x])
        
        return stack
        
class Solution2(object):
    def outterTree(self,points):
        def oriantation(p,q,r):
            return (p.y-q.y)*(r.x-p.x) - (r.y-p.x)*(q.x-p.x)
        
        stack = []
        points.sort(key = lambda p: (p.y, p.x))
        for i in range(len(points)):
            while (len(points)>=2 and oriantation(stack[-2],stack[-1],points[i] >0 ):
                stack.pop()
            stack.append(points[i])
        points.reverse()
        for i in range(len(points)):
            while (len(points)>=2 and oriantation(stack[-2],stack[-1],points[i] >0 ):
                stack.pop()
            if points[i] not in stack:
                stack.append(points[i])
        return stack
                   
        #第二种方法                   
        hull = []
        points.sort(key=lambda p: (p.x, p.y))

        for i in itertools.chain(xrange(len(points)), reversed(xrange(len(points)))):
            while len(hull) >= 2 and orientation(hull[-2], hull[-1],  points[i]) > 0:
                hull.pop()
            hull.append(points[i])

        return list(set(hull))
        
        

class Solution:
  def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
    hull = []

    trees.sort(key=lambda x: (x[0], x[1]))

    def cross(p: List[int], q: List[int], r: List[int]) -> int:
      return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    # Build lower hull: left-to-right scan
    for tree in trees:
      while len(hull) > 1 and cross(hull[-1], hull[-2], tree) > 0:
        hull.pop()
      hull.append(tuple(tree))
    hull.pop()

    # Build upper hull: right-to-left scan
    for tree in reversed(trees):
      while len(hull) > 1 and cross(hull[-1], hull[-2], tree) > 0:
        hull.pop()
      hull.append(tuple(tree))

    # Remove redundant elements from the stack
    return list(set(hull))
