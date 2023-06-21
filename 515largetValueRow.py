# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:26:20 2020

@author: liuga
"""

import collections

class Solution(object):
    def largestValuerow(self, root):
        
        q = collections.deque() #或者 q = collections.deque([root])
        q.append(root)
        res = []
        while q:
            n = len(q)
            
            max_level = float("-inf")
            for i in range(n):
                node = q.popleft()
                '''' 可以省略
                if not node:
                    continue
                '''
                max_level = max(max_level, node.val)
                q.append(node.left)
                q.append(node.right)
            if max_level != float("-inf"):
                res.append(max_level)
                
        return res

#此解法为主
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            maxi = -math.inf
            for _ in range(len(q)):
                root = q.popleft()
                maxi = max(maxi, root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            ans.append(maxi)

      return ans
