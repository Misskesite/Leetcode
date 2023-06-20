# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:22:12 2019

@author: liuga
"""
#时间复杂度O(n), 空间复杂度O(n)
class Solution(object):
    def isvalidBST(self, root):
        stack = []
        prev = float('-inf') #记录前一个节点值
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left     #左
                
            if stack: #这一句可以不要？因为while 里面有stack条件
                root = stack.pop()   #中
                if root.val <= prev:
                    return False
                prev = root.val
                root = root.right    #右
        return True


#递归，中序遍历，一直更新pre
class Solution2(object):
    def isValidBST(root):
        pre = float('-inf')
        if not root:
            return True    #二叉搜索树也可以为空
        
        if not isValidBST(root.left):
            return False
        
        #访问当前节点：如果当前节点小于等于中序遍历的前一个节点，说明不满足BST，返回 false；否则继续遍历
        if root.val <= pre:
            return False
        pre = root.val  #当pre小于root.val时候更新

    '''
       pre = None
       if pre:
            if root.val <= pre:
            return False
        pre = root.val   #一直更新pre
        
    '''

        return isValidBST(root.right)
    
class Solution3(object):
    def isvalidBST(self, root):
        if not root:
            return True

        def inOrder(root, order):
            if not root:
                return
            inOrder(root.left, order)
            order.append(root.val)
            inOrder(root.right, order)

        order = []
        inOrder(root, order)
        for i in range(1, len(order)):
            if order[i] <= order[i-1]:
                return False
        return True
    
