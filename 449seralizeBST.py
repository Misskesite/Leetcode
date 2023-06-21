# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:46:20 2020

@author: liuga
"""
#时间复杂度都是O(n) 二叉树转化为一个字符串，并且还能把这个字符串还原成原来的二叉树 输入root = [2,1,3] 输出[2,1,3]
import collections

class TreeNode(object):
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
#类似297, 297用##分隔，所以 build() 不需要设置参数        
class Solution(object):
    def serialize(self, root):
        res = []
        def preorder(root):
            if root:
                res.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ' '.join(res)
    
    def deserialize(self, data):
        nums = deque(int(n) for n in data.split())
        
        def build(minval, maxval):
            if nums and minval < nums[0] < maxval:
                n = nums.popleft()
                root = TreeNode(n)
                root.left = build(minval, n)
                root.right = build(n, maxval)
                return root
        return build(float('-inf'), float('inf'))


#先序遍历序列化，因为是二叉搜索树，所以排序后就是中序遍历，因此反序列化就转换成了105题的从先序与中序构造二叉树的问题
    class Codec:
    def serialize(self, root):
        def preorder(root):
            res = []
            if root:
                res += [str(root.val)]
                res += preorder(root.left)
                res += preorder(root.right)
            return res
        return ','.join(preorder(root))
        
    def deserialize(self, data):
        if not data:
            return None
        def buildTree(pre_o, in_o):
            if not pre_o:
                return None
            mid = pre_o[0]
            i = in_o.index(mid)
            root = TreeNode(mid)
            root.left = buildTree(pre_o[1:i + 1], in_o[:i])
            root.right = buildTree(pre_o[i + 1:], in_o[i + 1:])
            return root
        pre_o = list(map(int, data.split(',')))
        in_o = sorted(pre_o)
        return buildTree(pre_o, in_o)



class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def preorderTraversal(root):#前序遍历
            if root == None:
                return  []
            left = preorderTraversal(root.left)
            right = preorderTraversal(root.right)
            return [root.val] + left + right
        L = preorderTraversal(root)
        return ' '.join([str(i) for i in L])#转化为字符串

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = data.split()
        data = [int(i) for i in data]#将字符串转化为数值的列表
        
        def buildTree(data):
            if not data:
                return None
            root = TreeNode(data[0])
            left = [i for i in data if i < data[0]]#左子树的节点值小于根节点
            right = [i for i in data if i > data[0]]#右子树的节点值大于根节点的值
            root.left = buildTree(left)#重建左子树
            root.right = buildTree(right)#重建右子树
            return root
        return buildTree(data)
