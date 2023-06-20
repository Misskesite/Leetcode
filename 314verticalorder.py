# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:32:58 2020

@author: liuga
"""
import collections

class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return []
        cols = collections.defaultdict()
        q = [(root,0)]
        while q:
            for node, col in q:
                cols[col].append(node.val)
            new_q = []
            for node, col in q:
                if node.left:
                    new_q.append((node.left, col-1))
                if node.right:
                    new_q.append((node.right, col+1))
            q = new_q
        
        return [cols[k] for k in sorted(cols.keys())]
            
                    
        
#改写
import collections
import deque

class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return []
        mp = collections.defaultdict(list)
        queue = collections.deque([(root,0)])

 
        res = []

        while queue:
            node, col = queue.poleft()
            mp[col].append(node.val)

            if node.left:
                queue.append((node.left, col -1))
            if node.right:
                queue.append((node.right, col+1))

        for k in sorted(cols.keys()):
            res.append(mp[k])

        return res
