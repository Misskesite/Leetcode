# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:00:10 2020

@author: liuga
"""
import collections

class Solution(object):
    def sortFrequency(self, s):
        count = collections.Counter(s).most_common() # n 个最常见的元素及出现次数，按常见程度由高到低排序. n缺省则为全部
        res = ''
        for c,v in count:
            res += c*v
        return res


class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        items = [(-val, key) for key, val in count.items()]
        heapq.heapify(items)
        res = ""
        while items:
            val, key = heapq.heappop()
            res += key * (-val)
        return res

