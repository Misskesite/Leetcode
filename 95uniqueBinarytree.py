# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:05:11 2019

@author: liuga
"""
class TreeNode(object):
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
        
#二叉树性质 左子树的所有值小于根节点，右子树的所有值大于根节点，依次把1，2，3，4等作为根节点        
#生成一棵二叉树需要O(n)的时间复杂度，一共有Gn棵二叉树，时间复杂度O(nGn)
#根节点的值i比left小的时候，左子树为空
class Solution(object):
    def uniqueBinarytree(self, n):
        if n == 0:
            return []
        mp = dict()
        return self.dfs(1, n, mp)
    
    def dfs(self, left, right, mp):
        if left > right:
            return [None] #None是一个对象，NoneType
        
        res = []

        key = left + '-' + right
        if key in mp:
            res.append(mp[key])
        else:
            for i in range(left, right+1):
                left_nodes = self.dfs(left, i-1, mp)
                right_nodes = self.dfs(i+1, right, mp)
                
                for left_node in left_nodes:
                    for right_node in right_nodes:
                        #res.append(TreeNode(i, left_node, right_node))
                        root = TreeNode(i)
                        root.left = left_node
                        root.right = right_node
                        res.append(root)
        mp[key] = res
        return res

'''
n = 3
[1,null,3,2]
[3,2,null,1]
[3,1,null,null,2]
[2,1,3]
[1,null,2,null,3]
'''

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        mp = {}
        def generateTrees(mini: int, maxi: int) -> List[Optional[int]]:
            if mini > maxi:
                return [None]

            ans = []
            if (mini, maxi) in mp:
                return  mp[(mini, maxi)]  
            else:
                for i in range(mini, maxi + 1):
                    for left in generateTrees(mini, i - 1):
                        for right in generateTrees(i + 1, maxi):
                            ans.append(TreeNode(i))
                            ans[-1].left = left
                            ans[-1].right = right
            mp[(mini, maxi)] = ans
            return ans

        return generateTrees(1, n)
