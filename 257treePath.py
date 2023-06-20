# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:15:01 2020

@author: liuga
"""
#时间复杂度O(n*n)
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root:TreeNode, path:str, res:List[str]):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                res.append(path)
            else:
                path += '->'
                dfs(root.left, path, res)
                dfs(root.right, path, res)
            return res
        return dfs(root, '', [])

class Solution:
    def binaryTreePaths(self, root):
        def dfs(root, path):
            if root:                    #当前节点存在
                path += str(root.val)   #当前节点的值加入路径中
                if not root.left and not root.right:    #叶子节点，将路径加入返回值
                    res.append(path)
                else:
                    path += "->"        #非叶子节点，继续递归添加
                    dfs(root.left, path)
                    dfs(root.right, path)
        res = []
        dfs(root, "")
        return res


#简写
class Solution2(object):
    def treePath(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, res, '')
        return res
        
    def dfs(self, root, res, path):
        if not root: #遍历到空节点，结束当前递归分支
            return 
        if root.left == None and root.right == None: #遍历到叶子节点
            path += str(root.val)
            res.append(path)
            return

        path += str(root.val) + '->'  #处理非叶子节点，加箭头
        self.dfs(root.left, res, path)
        self.dfs(root.right, res, path)

#此法为主
def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return 
        queue = deque()
        res = []
        queue.append((root, str(root.val)))
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right :
               
                res.append(path)
            if node.left:
                queue.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + "->"+ str(node.right.val)))
        return res
