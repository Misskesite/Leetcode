# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:16:59 2020

@author: liuga
"""
#时间复杂度 O(n)
# 1 target的值比集合中最小的值小, 因为中序遍历是有序的, 最小元素就是第0个元素
# 2 target的值大于集合中的最小值，小于最大值
# 3 target的值大于集合中的最大值。 当集合中的元素大于k时，我们需要元素替换,第一种情况无法替换,第0个最近，元素有序
# 第2，3种情况，我们用当前值和集合中的最小值比较，如果当前值更靠近target，就替换最小的值
#O(n)
class Solution(object):
    def closestKvalues(self, root, target, value, k):
        result = []
        index = 0
        if not root:
            return
        self.closestKvalues(root.left, target, value, k)
        if len(result) < k:
            result.append(root.val)
        #替换
        elif abs(target - result[index]) < abs(target - root.val):
            result[index + 1] = root.val
            index = index + 1
            if index == k:
                index = 0
        else:
            return result
        self.closestKvalues(root.right, target, value, k)
        return result

#以此解法为主 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        q = deque()

        def inorder(root: Optional[TreeNode]) -> None:
            if not root:
                return

            inorder(root.left)
            q.append(root.val)
            inorder(root.right)

        inorder(root)

        while len(q) > k:
            if abs(q[0] - target) > abs(q[-1] - target):
                q.popleft()
            else:
                q.pop()

        return list(q)
                
        
#用tree iterator包括forward和backward方向，定位closest node来初始化这两个iterator需要O(log(n))时间
#向两个方向扩展k次,时间复杂度O(logn + k) 空间复杂度logn
class Solution2(object):
    def closestKvalues(self, root, target, k):
        res = []
        if not root:
            return
        preOrder = []
        postOrder = []

        def findTarget(preOrder, PostOrder, root, target):
            node = root
            while node:
                if node.val < target:
                    preOrder.append(node)
                    node = node.right
                else:
                    postOrder.append(node)
                    node = node.left

        def getSuccessor(postOrder, res):
            node = postOrder.pop()
            res.append(node.val)
            if node.right:
                n = node.right
                while n:
                    postOrder.append(n)
                    n = n.left

        def getPredecessor(preOrder, res):
            node = preOrder.pop()
            res.append(node.val)
            if node.left:
                n = node.left
                while n:
                    preOrder.append(n)
                    n = n.right
                       
                    

        findTarget(preOrder, postOrder, root, target)
        while  k > 0:
            if ( not preOrder) or (PreOrder and target - preOrder[0].val < PostOrder[0].val - Target:
                getPredecessor(preOrder, res)
            else:
                getSuccessor(postOrder, res)
            k -= 1

        
        
