# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:25:19 2020

@author: liuga
"""
#分治法，对左右节点分别处理
class Solution(object):
    def consecutiveLongest(self, root):
        if not root:
            return 0
        self.res = 0
        
        def dfs(self, node, cur_Len):
            self.res = max(self.res, cur_Len)
            if node.left:
                if node.val + 1 == node.left.val:
                    self.dfs(node.left, cur_Len + 1)
                    
                else:
                    self.dfs(node.left, 1)
            
            if node.right:
                if node.val + 1 == node.right.val:
                    self.dfs(node.right, cur_Len + 1)
                    
                else:
                    self.dfs(node.right, 1)
                
        dfs(root, 1)
        return self.res
    
#path need to be from parent to child   #先序遍历 从根到叶子节点
class Solution2(object):
    def longestConsecutive(self, root):
        if not root:
            return 0

        self.res = 0

        def dfs(node, cur_Len, parent): #parent记录父节点
            if not node:
                return
            if node.val == parent.val + 1:
                cur_Len += 1                

            else:
                cur_Len = 1                 #不能构成，重置计数器

            self.res = max(self.res, cur_Len)

            dfs(node.left, cur_Len, node)
            dfs(node.right, cur_Len, node)

        dfs(root, 0, root)        

        return self.res


