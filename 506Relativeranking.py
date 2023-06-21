# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:59:59 2020

@author: liuga
"""

#利用堆自动排序
import heapq

class Solution(object):
    def findRelativeRank(self, nums):
        heap = [(-num,i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        n = len(nums)
        res = [""]*n
        cnt = 1
        while heap:
            num,i = heapq.heappop(heap)
            if cnt == 1:
                res[i] = "Gold Medal"
            elif cnt == 2:
                res[i] = "Silver Medal"
            elif cnt == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(cnt)
            cnt += 1
        return res
                
        
#排序+哈希表
class Solution2(object):
    def findRelativeRank(self, nums):
        ranks = sorted(score, reversed = True)
        ranksIndex = dict()
        for i in range(len(ranks)):
            ranksIndex[ranks[i]] = i

        res = []
        for s in score:
            rank = ranksIndex[s]
            if rank == 0:
                res.append("Gold Medal")
            elif rank == 1:
                res.append("Silver Medal")
            elif rank == 2:
                res.append("Bronze Medal")
            else:
                res.append(str(rank + 1)) #数组下标从0开始，排名从1开始
        return res
                
