# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:01:53 2020

@author: liuga
"""
235是BST( Binary Search Tree) 236 是 Binary Tree
#通过递归对二叉树进行先序遍历，终止条件: 越过叶节点，直接返回null, root等于p ,q时，直接返回root    
# 返回值四种情况: 1 left和 right同时为空,说明root的左右子树都不包含p, q 返回Null 2 同时不为空, 说明在2侧， 返回root
#3 left 为空 ，right不为空 ：p, q都不在 root的左子树中，直接返回 right(p, q其中一个(p)在root的右子树里，right指向p)(p,q两个都在右子树里，right指向最近公共祖先节点)
#4 left不为空, right为空，类似于3
#时间复杂度O(N),最差情况遍历树的所有节点，空间复杂度O(N),最差情况递归深度

class Solution(object):
    def lowestancestor(self, root, p, q):
        if not root or p == root or q == root:
            return root
        # Find p/q in left subtree
        left = self.lowestancestor(root.left, p, q) #因为是递归，使用函数后可认为左右子树已经算出p,q的公共祖先
        # Find p/q in right subtree
        right = self.lowestancestor(root.right, p, q)

        # If p and q found in left and right subtree of this node, then this node is LCA
        if left and right: #说明在2侧
            return root
        #Else return the node which returned a node from it's subtree such that one of it's ancestor will be LCA
        return left if left else right

'''
        if not left and not right:
            return None      # 1. 第一种可以合并到第3，4种
        if not left:
            return right # 3.
        if not right:
            return left  # 4.
        return root      # 2. if left and right:


'''

class Solution2(object):
    def lowestancestor(self, root, p, q):
        if not root :
            return None
        if root.data > p and root.data > q:
            return lowestancestor(root.left, p, q)
        if root.data < p and root.data < q:
            return lowestancestor(root.right, p, q)
        
        return root
        
