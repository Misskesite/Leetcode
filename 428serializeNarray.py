# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:20:32 2020

@author: liuga
"""
#BFS N叉树跟2叉树的区别是会把children的size说明
#此解法为主
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                return

            res.append(str(root.val))
            for ch in root.children:
                dfs(ch)
            res.append("#")
        dfs(root)
        return ",".join(res)
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return

        res = deque(data.split(","))
        root = Node(int(res.popleft()), [])

        def dfs(node):
            while res[0] != "#": # add child nodes with subtrees
                child = Node(int(res.popleft()), [])
                node.children.append(child)
                dfs(child)
            res.popleft()
        dfs(root)
        return root

    #简化
    def deserialize(self, data: str) -> 'Node':
       
        if not data:
            return
        
        res = deque(data.split(","))        

        def dfs():
            root = Node(int(res.popleft()), [])
            while res[0] != "#": # add child nodes with subtrees                
                
                root.children.append(dfs())
            res.popleft()
            return root
        return dfs()
                    
                    
#DFS 1(3) 3 (2) 5 (0) 6 (0) 2 (0) 4 (0)
class Solution2(object):
    def serialize(self, root:'Node'): -> str
        res = [] 
        def dfs(root):
            if not root:
                return

            res.append(str(root.val))
            res.append(str(len(root.children)))
            for ch in root.chilren:
                    dfs(ch)

        dfs(root)
        return ",".join(res)


    def deserialize(self, data):
        if not data:
            return 

        data = iter(data.split(","))

        def dfs():
            root = Node(int(next(data)), [])
            num = int(next(data))
            for _ in range(num):
                root.children.append(dfs()) #每个dfs调用return一个node
            return root

        return dfs()
                    
#改写
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                return

            res.append(str(root.val))
            res.append(str(len(root.children)))
            for ch in root.children:
                dfs(ch)

        dfs(root)
        return ",".join(res)
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return

        res = deque(data.split(","))

        def dfs():
            
            root = Node(int(res.popleft()), [])
            num = int(res.popleft())
            for _ in range(num):
                root.children.append(dfs())
            return root
        
        return dfs()
                    
        
