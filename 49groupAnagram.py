# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 22:16:58 2019

@author: liuga
"""

class Solution(object):
    def groupAnagram(self, strs):
        map = {}
        for i, v in enumerate(strs):
            target = "".join(sorted(v))
            
            if target not in map:
                map[target] = [v]
            else:
                map[target].append(v)               
                
        result = []
            
        for value in map.values():
            result += [sorted(value)]
                
        return result

    
#时间复杂度O(nklogk) n是字符串数量，k是字符串最大长度，每个字符串需要klogk时间排序
import collections
class Solution(object):
    def groupAnagams(self, strs):
        res = collections.defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            res[key].append(str)

        return res.values()
