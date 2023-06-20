# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:16:42 2019

@author: liuga
"""
#和上一题116的区别是普通二叉树
class TreeLinkNode(object):
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
        
class Solution(object):
    def connect(self, root):
        dummy = TreeLinkNode(-1)
        node = dummy
        while root:
            while root:
                node.next = root.left
                node = node.next or node
                node.next = root.right
                node = node.next or node
                root = root.next
            root, node = dummy.next, dummy
                

#当我们层历遍完了，dummy的next就是下一层最左边的node
class Solution2(object):
    def connect(self, root):
        if not root:
            return None
        cur = root
        while cur:
            dummyHead = Node(-1)  #下一行之前的节点
            pre = dummyHead
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            cur = dummyHead.next #换行操作，更新到下一行
        return root
