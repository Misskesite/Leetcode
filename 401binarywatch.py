# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:29:40 2020

@author: liuga
"""
#输入turnedOn = 1，表示亮着的LED的数量
import combinations

class Solution(object):
    def binarywatch(self, num):
        res = []
        self.dfs(num,0, res)
        return res
    
    def dfs(self, num, hours, res):
        if hours > num:
            return
        for hour in combinations([1,2,4,8], hours):
            hs = sum(hour)
            if hs >= 12:
                continue
            for m in combinations([1,2,4,8,16,32],num-hours):
                mins = sum(m)
                if mins > 60:
                    continue
                res.append("%d：%02d" % (hs,mins))
            self.dfs(num, hours+1, res)
        
            
#直接遍历0：00 - 12：00每个时间有多少个1
class Solution(object):
    def readBinary(num):
        res = []
        
        def count1(n):
            cnt = 0
            while n:
                n = n&(n-1)
                cnt += 1
                # n&1 == 1: cnt += 1; num >= 1
            return cnt
            
        for i in range(12):
            for j in range(60):
                if count1(i) + count(j) == num:
                    res.append(str(i) + ":" + (("0" + str(j) if j < 10 else str(j))
                        
        
