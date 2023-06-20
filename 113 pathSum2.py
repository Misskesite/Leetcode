# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:49:53 2019

@author: liuga
"""
#是否要回溯：二叉树的问题大部分是不需要回溯的，原因如下：
#二叉树的递归部分：dfs(root->left),dfs(root->right)已经把可能的路径穷尽了，到任意叶节点的路径只可能有一条，绝对不可能出现另外的路径也到这个满足条件的叶节点的


class TreeNode(object):
    def _init_(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def hasPathsum (self, root, sum):
        result = []
        self.dfs(root, sum, [], result)
        return result
    
    def dfs(self, root, sum, path, result):
        
         if not root:
            return 
         
         if not root.left and not root.right:
             if sum == root.val:
                 result.append(path + [root.val])
                 return
        
         
         self.dfs(root.left, sum - root.val, path + [root.val], result) 
           
         self.dfs(root.right, sum - root.val, path + [root.val], result)


#BFS
import deque
class Solution2(object):
    def pathSum(self, root, s):
        res = []
        que = deque()
        que.append((root, [], 0))

        while que:
            node, path, pathsum = que.popleft()
            if not node:                         #空节点，不处理
                continue

            if not node.left and not node.right: #叶子节点
                if node.val + pathSum == s:      #加上叶子节点，路径和等于sum
                    res.append(path + [node.val])#保存路径
            #处理左子树
            if node.left:
                que.append((node.left, path + [node.val], pathsum + node.val))
            #处理右子树
            if node.right:
                que.append((node.right, path + [node.val], pathsum + node.val))

        return res
            
                
