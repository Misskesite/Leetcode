# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:15:47 2020

@author: liuga
"""


#后继结点出现的位置大致可以分为两类，一类是(某个结点存在右子结点时)在子孙结点中，没有右节点另一类是在第一个比其值大的祖先结点中。
class Solution(object):
    def inorderSuccessor(self, node):
        if not node:
            return
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
        '''
        while node.parent and node.parent.left != node:
            node = node.parent
        return node.parent

        '''
        
            parent =  node.parent
            while parent and parent.left != node: #不是父节点的左孩子,是右节点
                node = parent
                parent = node.parent
            return parent #父节点的左子孩子？
        
 
#当右子结点存在时，我们需要找到右子结点的最左子结点，就用个 while 循环就行了。
#当右子结点不存在，我们就要找到第一个比其值大的祖先结点，也是用个 while 循环去找即可
class Solution(object):
    def inorderSuccessor(self, node):
        if not node:
            return
        #有右子节点
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        #没有右子节点(和上面的写法类似) 找到第一个比它大的祖先节点
        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent


class Solution3(object):
    def inorderSuccessor(self, node):
        if not node:
            return
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        while node:
            if not node.parent: #最右子节点，往上找不到root的parent(祖先节点) 为空
                return
            if node == node.parent.left:
                return node.parent
            node = node.parent
        return node
        
