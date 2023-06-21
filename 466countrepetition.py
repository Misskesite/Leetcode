# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:25:09 2020

@author: liuga
"""
import collections

class Solution(object):
    def countRepetition(self,s1,n1,s2,n2):
        if not set(s2) < set(s1):
            return 0
        l1,l2 = len(s1), len(s2)
        dp = collections.defaultdict(dict)
        x1 = x2 = 0
        while x1 < l1*n1:
            while s1[x1 % l1] != s2[x2 % l2]:
                x1 += 1
                if x1 >= l1*n1:
                    break
                y1, y2 = x1%l1, x2%l2
                if y2 not in dp[y1]:
                    dp[y1][y2] = x1, x2
                else:
                    dx1,dx2 = dp[y1][y2]
                    round = (l1*n1-dx1)/(x1-dx1)
                    x1 = dx1 + round*(x1-dx1)
                    x2 = dx2 + round*(x2-dx2)
                if x1 < l1*n1:
                    x1+=1
                    x2+=1
            return x2/(n2*l2)
                    
                    
#贪心+拼接 找出循环 dic哈希表 dic[i] = [cnt, index]表示s2从s2[i]开始匹配完一个完整的s1后，经过cnt个s2，最后s2的索引会从index开始
class Solution2(object):
    def getMaxrepetition(self, s1, n1, s2, n2):
        m = len(s1)
        n = len(s2)
        dic = {}
        for i in range(n):
            cnt = 0
            index = i
            for j in range(m):
                if s1[j] == s2[index]:
                    index += 1
                if index == n: #匹配完
                    cnt += 1
                    index = 0
            dic[i] = [cnt, index]

        res = 0
        j = 0
        for i in range(n1):
            cnt, j = dic[j]
            res += cnt
        return res//n2
            
