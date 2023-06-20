# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:23:34 2019

@author: liuga
"""
#展开后的链表和先序遍历相同,
class Solution(object):
    def flattenBST(self, root):
        res = []
        self.preorder(root, res)
        for i in range(len(res)-1):
            pre , cur = res[i], res[i+1]
            pre.left = None
            pre.right = cur
            
    def preorder(self, root,res):
        if not root:
            return
        res.append(root)
        self.preorder(root.left, res)
        self.preorder(root.right, res)
        

#连接左右两边右两个思路：要么记录左子树的最后一个节点，要么记录右子树的 root 节点

class Solution2(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.last = None
        def traverse(root):
            if not root:
                return
            traverse(root.right)
            traverse(root.left)
            
            root.right = self.last
            root.left = None
            self.last = root #后序遍历,借助一个辅助结点记录上个结点即可
        traverse(root)

    #输入是根节点，函数把根节点下的所有孩子按照先序遍历放在其右侧
    #把左右子树flatten成两个链表，然后根节点的左孩子放在根节点的右孩子上，原来根节点的右孩子拼到根节点的链表结尾
        1
     2     5
    3  4     6
    先变成3 2-4 1-5-6
    变成 2-3-4  1-5-6
    再变成1-2-3-4-5-6
    def flatten(root):
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        if root.left: #左子树最右的节点
            pre = root.left
            while pre.right:
                pre = pre.right

            pre.right = root.right #pre对应lefttail
            root.right = root.left
            root.left = None
