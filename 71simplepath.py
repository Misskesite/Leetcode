# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:27:08 2019

@author: liuga
"""
#linux里面的目录用栈来实现 时间 空间复杂度O(n)
class Solution(object):
    def simplyPath(self, path):
        stack = []
        dirs = path.split('/')
        
        for dir in dirs:
            if not dir or dir == '.':   # if dir in ("", ".")         
                continue
            
            if dir == '..':
                if stack:
                    stack.pop()
                    
            else:
                stack.append(dir)
                    
        return '/'+ '/'.join(stack)
            
            
