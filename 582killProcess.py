# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:04:19 2020

@author: liuga
"""

import collections

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        dic = defaultdict(list)
        for child, parent in zip(pid, ppid):
            dic[parent].append(child) #找到对应的父节点， parentID -> a list of childrenIDs
        
        queue = deque([kill])
        res = []
        while queue:
            first = queue.popleft()
            res.append(first)
            for child in dic[first]:
                queue.append(child)
        return res
        
        
        
