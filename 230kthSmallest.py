# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 17:09:24 2019

@author: liuga
"""
#时间复杂度O(h+k) 需要递归找到最小的节点再开始数k个节点， 空间复杂度O(h)
class Solution(object):
    def inorder(root):
        if not root:
            return
        self.inorder(root.left)
            
        self.cnt -= 1
        if self.cnt == 0:
            self.res = root.val
            return
        self.inorder(root.right)

    #使用全局变量        
    def kthlargest(self, root, k):
        self.res = 0
        self.cnt = k        
        self.inorder(root)
        return self.res

#改写，更快
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.cnt = k
        self.res = None
        self.found = False
        self.helper(root)
        return self.res

    def helper(self, node):
        #exit as soon as possible
        if self.found:
            return
        if not node:
            return
        self.helper(node.left)
        self.cnt -= 1
        if self.cnt == 0:
            self.res = node.val
            self.found = True
            return
        self.helper(node.right)
        
    
#时间复杂度O(N),遍历整个数， 空间复杂度O(N), 用一个数组存储中序序列
class Solution2(object):
    def kthSmallest(self, root, k):
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        return inorder(root)[k-1]
    '''
    def kthSmallest(self, root, k):
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        return res[k-1]

    '''
    

#迭代，栈.可以加快速度, 不用遍历整个树,找到答案后停止 [5 3 2 4 6]
#时间复杂度O(H+k) H为树的高度，当树是平衡树时(logN + k) 空间复杂度O(H + k)
class Solution3(object):
    def kthSmallest(self, root, k):
        
        stack = []
        
        while True:
            while root:
                stack.append(root) #单调栈？栈里面的数字是单调递减的
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
