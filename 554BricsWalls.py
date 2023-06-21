# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:24:39 2020

@author: liuga
"""
import collections
#the goal is to find where the most brick edges line up(distance of edge from the left-most point)
class Solution(object):
    def leastBricks(self, wall):
        left_cnt = collections.Counter()
        count = 0
        for row in wall:
            left = 0
            for i in range(len(row)-1):
                left += row[i]
                left_cnt.update([left])
                count = max(count, left_cnt[left])
        return len(wall) - count
    
#"穿过的砖块数量加上从边缘经过的砖块数量之和是一个定值, 哈希表(缝隙到左侧边缘的距离(砖块的累计宽度，即前缀和prefixsum):穿过空格的数目)
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        mp = defaultdict(int)
        overlaps = 0
        for row in wall:
            pos = 0
            for i in range(len(row)-1):
                pos += row[i]
                mp[pos] += 1
                overlaps = max(overlaps, mp[pos])

        return len(wall) - overlaps

#The path that cuts through the minimum number of bricks is the path that passes through the most brick edges/endpoints.
#we use a map  we count  each brick edge distance from the left-most point ,how many times each brick ends on the same point
number of brick edges at that index
