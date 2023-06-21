# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:46:39 2020

@author: liuga
"""
#曼哈顿距离 如果松鼠和树重合，距离不变
class Solution(object):
    def minimumDistance(self, height,width,tree,squirrel, nuts):
        manhatten = lambda p,q : abs(p[0]-q[0]) + abs(p[1]-q[1])
        total = 2*sum(manhatten(tree, nut) for nut in nuts)
        return total + min(manhatten(squirrel,nut) - manhatten(tree,nut) for nut in nuts) #松鼠到坚果距离和坚果到树的距离差
    
#每次只能带一个坚果到树下，那么除了第一个要捡的坚果外，从树出发，捡其他每一个坚果的距离都要乘以2（从树到坚果i的距离 + 从坚果i到树的距离）

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def dist(a: List[int], b: List[int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

    totDist = sum(dist(nut, tree) for nut in nuts) * 2
    maxSave = max(dist(nut, tree) - dist(nut, squirrel) for nut in nuts)
    return totDist - maxSave
