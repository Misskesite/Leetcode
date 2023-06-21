# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:09:47 2020

@author: liuga
"""
#众数，频率最大的数 寻找出现最多次的数字
import collections

class TreeNode(object):
    def _init_(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        self.count = collections.Counter()
        self.inorder(root)
        freq = max(self.count.values()) #用defauldict dicval_list = list(dic.values())    maxi = max(dicval_list)   # find maximum value in dictionary
                
        res = []
        for item, c in self.count.items():
            if c == freq:
                res.append(item)
        return res
                
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.count[root.val] += 1
        self.inorder(root.right)


#follow up 用O(1)的空间复杂度 中序遍历，遍历2次
class Solution(object):
    def _init_(self):
        self.pre = None
        self.res = []
        self.res_count, self.max_count, self.cur_count = 0 ,0 ,0

    def findMode(self, root):
        self.inOrder(root)
        self.pre = None
        self.res = [0]*self.res_count
        self.res_count, self.cur_count = 0, 0
        self.inOrder(root)
        return self.res

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        if self.pre and self.pre.val == root.val:
            self.cur_count += 1
        else:
            self.cur_count += 1

        if self.cur_count > self.max_count:
            self.max_count = self.cur_count
            self.res_count = 1
        elif self.cur_count = self.max_count:
            if len(self.res):
                self.res[self.cur_count] = root.val
            self.res_count += 1
        self.pre = root
        self.inOrder(root.right)

    #改写
    def findMode(self, root):
        self.count = 0
        self.maxCount = 0
        self.pre = None
        self.res = []
        
        def searchBST(cur: TreeNode):
            if cur == None: #叶子节点返回
                return
            
            searchBST(cur.left)
            if self.pre == None:          #第一个节点
                self.count = 1
            elif self.pre.val == cur.val: #与前一个节点值相同
                self.count += 1
            else:
                self.count = 1
            self.pre = cur

            if self.count == self.maxCount:
                self.res.append(cur.val)
            if self.count > self.maxCount:
                self.maxCount = self.count
                self.res = [cur.val]
                '''
                self.res = list() #重置？更新
                self.res.append(cur.val)
                '''
            
            searchBST(cur.right)
            return
        
        searchBST(root)
        return self.res

