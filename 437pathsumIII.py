# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:40:41 2020

@author: liuga
"""
#时间复杂度O(n*n)
class Solution(object):
    def pathsum(self, root, targetSum):
        if not root:
            return 0
        return self.dfs(root, targetSum) + self.pathsum(root.left, targetSum) + self.pathsum(root.right, targetSum) #一个从根节点出发，另外2个从左右节点出发？
    
    def dfs(self, root, targetSum):
        res = 0
        if not root:
            return res
        if targetSum == root.val
            res += 1
        res += self.dfs(root.left, targetSum) 
        res += self.dfs(root.right, targetSum)
        return res


class Solution {
public:
    int pathSum(TreeNode* root, int sum) {
        if (!root) return 0;
        return sumUp(root, 0, sum) + pathSum(root->left, sum) + pathSum(root->right, sum);
    }
    int sumUp(TreeNode* node, int pre, int& sum) {
        if (!node) return 0;
        int cur = pre + node->val;
        return (cur == sum) + sumUp(node->left, cur, sum) + sumUp(node->right, cur, sum);
    }
};

    
class Solution2:
    def pathSum(self, root, sum):
        def dfs(root, sumlist):
            if root is None: 
                return 0
            sumlist = [num + root.val for num in sumlist] + [root.val]
            return sumlist.count(sum) + dfs(root.left, sumlist) + dfs(root.right, sumlist)
        return dfs(root, [])


#前缀和 每一条路径上求解：两个节点之差等于 targetSum，边遍历边计算前缀和。
#时间复杂度O(n)每个节点遍历一遍， 空间复杂度O(n)
import collections
class Solution(object):
    def pathSum(self, root, targetSum):
        mp = collections.defaultdict()
        mp[0] = 1
       
        def dfs(node,curSum):
            if not node:
                return 0

            res = 0
            curSum += node.val
            res += mp[curSum - targetSum]

            mp[curSum] += 1

            res += dfs(root.left, curSum) #do DFS on the left and right child of the current node, with currSum being their prevSum. 
            res += dfs(root.right, curSum)

            mp[curSum] -= 1 #路径总和从哈希表中删除，防止影响统计到跨越两个方向的路径.  because the current node is not on the path of DFSs on other nodes, hence currSum is not available for other DFSs.

            return res
        return dfs(root, 0)

'''
we will have to think of a clear way to memorize the intermediate result. we did a lot repeated calculation. For example 1->3->5, we calculated: 1, 1+3, 1+3+5, 3, 3+5, 5.
we can create a dictionary (named cache) which saves all the path sum (from root to current node) and their frequency.

e traverse through the tree, at each node, we can get the currPathSum (from root to current node). If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target.
'''

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        def dfs(root, prevSum, targetSum):
            if not root:
                return 0
            count = 0
            currSum = prevSum + root.val
            if currSum - targetSum in rec:
                count += rec[currSum - targetSum]
            if currSum in rec:
                rec[currSum] += 1
            else:
                rec[currSum] = 1
            count += dfs(root.left, currSum, targetSum)
            count += dfs(root.right, currSum, targetSum
            rec[currSum] -= 1
            return count
            
        rec = {0:1}
        return dfs(root, 0, sum)
