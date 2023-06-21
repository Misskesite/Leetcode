# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:39:15 2020

@author: liuga
"""
class Treenode(object):
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
        
#root,(left),(right)        4(2(3)(1))(6(5))
class Solution(object):
    def str2Tree(self, s):
        if not s:
            return 
        n = ''
        while s and s[0] not in ('(',')'):
            n += s[0]
            s = s[1:]
        node = Treenode(int(n))
        left, right = self.divide(s)
        node.left = self.str2Tree(left[1:-1])
        node.right = self.str2Tree(right[1:-1])
        return node
    
    def divide(self,s):
        part = ''
        deg = 0
        while s:
            deg += {'(':1, ')':-1}.get(s[0],0)
            part += s[0]
            s = s[1:]
            if deg == 0:
                break
        return part, s
    
#example  "4(2(3)(1))(6(5))"
        
    
    def deserialise(self, s):
        if not s:
            return
        stack = [Treenode(0)]
        num = ''
        for i, c in enumerate(s):
            if c == ')':
                stack.pop()
            elif c != '(':
                num += c
                if i+1 == len(s) or not s[i+1].isdigit():
                    node = Treenode(int(num))
                    if stack[-1].left:
                        stack[-1].right = node
                    else:
                        stack[-1].left = node
                    stack.append(node)
                    num = ''
        res = stack[0].left
        
#example  "4(2(3)(1))(6(5))" 
#此法为主？
class Solution(object):
    def str2tree(self, s):
        if not s:
            return None

        if '(' not in s:
            return TreeNode(int(s))

        def paren_pair_idx(s):
            paren_cnt = 0
            for i in range(len(s)):
                if s[i] == '(':
                    paren_cnt += 1
                elif s[i] == ')':
                    paren_cnt -= 1

                if paren_cnt == 0 and i > s.find('('): #查找出现的第一个字符的index
                    return (s.find('('), i)

        root = TreeNode(int(s[:s.find('(')]))
        (parent_left, parent_right) = paren_pair_idx(s)
        root.left = self.str2tree(s[parent_left +1 : parent_right])
        root.right =  self.str2tree(s[parent_right+2 : -1]
        '''
        if parent_right < len(s) - 1: #这里可以不用判断，因为如果为空，自然会返回None
            root.right =  self.str2tree(s[parent_right+2 : -1])
        else:
            root.right = None
        '''
        return root

#上面改写
class Solution(object):
    def str2tree(self, s):
        if not s:
            return None
        found = s.find('(')        

        if found == -1:
            return TreeNode(int(s))

        root = TreeNode(int(s[:found]))
        start = found
        cnt = 0
        for i in range(start, len(s)):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1

            if cnt == 0 and start == found:
                root.left = str2tree(s[start +1 : i])
                start = i + 1
            elif cnt == 0:
                root.right = str2tree(s[start +1 : i])
        return root

    
    def str2tree(self, s):
        while s and s[0] not in ('(',')'):
            n += s[0]
            s = s[1:]
        root = Treenode(int(n))

        first = -1
        second = -1
        count = 0

        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                if count == 1:
                    if first == -1: #第一个左括号 #只需要求第一个左括号？
                        first = i
                    else:
                        second = i      #第二个左括号位置？
            elif s[i] == ')':
                count -= 1

        if first == -1:
            root.val = int(s)
        elif second == -1:
            root.val = int(s[:first])
            root.left = str2tree(s[first+1: -1])
            
        else:
            root.val = int(s[:first])
            root.left = str2tree(s[first+1: second+1])
            root.right = str2tree(s[second+1: -1])

        return root



class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        '''
        have a dfs function to walk through the string
        dfs(s, i), take string and start index
        build node then recursive calls to build node.left and node.right
        return node and index
        
        returning index because we do preorder traversal
        need next index to build node.right
        '''
        if not s or len(s) == 0:
            return None
        
        root, idx = self.dfs(s, 0)
        return root
        
    def dfs(self, s, i):
        start = i
        if s[start] == '-':
            i += 1
        while i < len(s) and s[i].isdigit():
            i += 1
        node = TreeNode(int(s[start:i]))
        
        if i < len(s) and s[i] == '(': 
            i += 1
            node.left, i = self.dfs(s, i)
            i += 1
        
        if i < len(s) and s[i] == '(':
            i += 1
            node.right, i = self.dfs(s, i)
            i += 1
        
        return node, i
        
