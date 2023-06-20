# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:39:39 2019

@author: liuga
"""

class Point(object):
    def _init_(self, a=0, b=0):
        self.x = a
        self.y = b
        
class Solution(object):
      def maxPoints(self, points):
          n = len(points)
          res = 0
          
          for i in range(n):
              lines = collections.defaultdict(int)
              same = 1
              for j in range(i+1, n):
                  if points[i].x == points[j].x and points[i].y == points[j].y:
                      same += 1
                      continue
                  dx = points[i].x - points[j].x
                  dy = points[i].y - points[j].y
                  delta = self.gcd(dx, dy)
                  lines[(dx/delta, dy/delta)] += 1
                  
                  res = max(res, (max(lines.value) if lines else 0 + same))
                  return res
              
        def gcd(self, x, y):
            return x if y == 0 else self.gcd(y, x % y)

        
class Solution2(object):
    def maxPoints2(self, points):
        n = len(points)
        if n < 3:
            return n
        
        res = -1
        for i in range(n):
            same = 1
            slope = {'inf':0}
            
            for j in range(i+1, n):
                dx, dy = points[i].x - points[j].x, points[i].y - points[j].y
                if dx == dy == 0:
                    same += 1
                elif dx == 0 :
                    slope['inf'] += 1
                else:
                    k = float(dy)/float(dx)
                    if k not in slope:
                        slope[k] = 1
                    else:
                        slope[k] += 1
         res = max(res, max(slope.values()) + same)
         return res
                
                    
    
        
