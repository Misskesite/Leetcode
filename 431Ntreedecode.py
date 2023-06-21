# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:06:31 2020

@author: liuga
"""
#DFS 右边第二个孩子开始，挂在第一个孩子的右节点上
class Solution(object):
    def encode(self, root):
        if not root:
            return
        newRoot = TreeNode(root.val)
        #if not root.children: return newRoot
        if root.children:
            newRoot.left = self.encode(root.children[0])
        #parent of the rest of children
        cur = newRoot.left

        #encode the rest of the children
        if len(root.children) == 1:
            return newRoot
        for node in root.children[1:]:
            cur.right = self.encode(node)
            cur = cur.right
        return newRoot

    def encode(self, root: 'Node') -> Optional[TreeNode]:
        if not root:
          return None

        rootTreeNode = TreeNode(root.val)
        if root.children:
            rootTreeNode.left = self.encode(root.children[0])

        # The parent for the rest of the children
        currTreeNode = rootTreeNode.left

        # Encode the rest of the children
        for i in range(1, len(root.children)):
            currTreeNode.right = self.encode(root.children[i])
            currTreeNode = currTreeNode.right

        return rootTreeNode

    #Decodes  binary tree to an n-ary tree.
    def decode(self, root: TreeNode):    #二叉树    
        if not data:
            return 
        rootNode = Node(data.val, []) 
        cur = data.left
        #if not cur: return rootNode 
        while cur:
            rootNode.children.append(self.decode(cur))
            cur = cur.right
        return rootNode


    def decode(self, root: Optional[TreeNode]) -> 'Node':
        if not root:
            return None

        rootNode = Node(root.val, [])
        currTreeNode = root.left

        while currTreeNode:
            rootNode.children.append(self.decode(currTreeNode))
            currTreeNode = currTreeNode.right

        return rootNode

   1
 3 2 4
5 6

   1
 3
5  2
 6   4
            
        
