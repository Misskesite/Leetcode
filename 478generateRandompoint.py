# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:05:28 2020

@author: liuga
"""
import math
import random

class Solution(object):
    def _init_(self, radius, x_center, y_center):
        self.r = radius
        self.x = x_center
        self.y = y_center
        
    def generatePoint(self):
        nr = math.sqrt(random.random())*self.r
        alpha = random.random()*2*3.141592653 #2*math.Pi
        newx = self.x + nr.math.cos(alpha)
        newy = self.y + nr.math.sin(alpha)
        return [newx, newy]

#一个半径为1的圆，点落在半径为x的圆内的概率为x^2 为了使点均匀分布， x = sqrt(U) 这样概率就是U
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        
    def randPoint(self) -> List[float]:
        theta = random.uniform(0, 2*math.pi) #在两个数之间任意取值
        r = sqrt(random.uniform(0, 1))*self.radius
        return [self.x_center + r*math.sin(theta), self.y_center + r*math.cos(theta)]




class Solution3(object):
    def _init_(self, radius, x_center, y_center):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        while True:
            x1 = uniform(self.x - self.r, self.x + self.r) #[x-r, x+r]
            y1 = uniform(self.y - self.r, self.y + self.r) #[y-r, y+r]
            if (x1 - self.x)**2 + (y1 -self.y)**2 <= self.r**2:
                return [x1, y1]
