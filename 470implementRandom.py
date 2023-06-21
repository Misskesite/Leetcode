# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:09:50 2020

@author: liuga
"""

class Solution(object):
    def rand10(self):
        return self.rand40()%10 +1
 
    
    def rand49(self):
        return 7*(rand7()-1) + rand7() -1
    
    def rand40(self):
        num = self.rand49()
        while num >=40:
            num = self.rand49()
        return num
        
        
    

#(randX() - 1)*Y + randY() 可以等概率的生成[1, X * Y]范围的随机数
#期望的时间复杂度O(1) 空间复杂度O(1)
class Solution(object):
    def rand10(self) -> int:
        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1)*7 + col
            if idx <= 40:
                return 1 + (idx - 1)%10

'''''
random10 映射到random7 可以选择的数组概率是7/10
1-7直接返回   概率 1/10
8-10重新映射, 概率 7/10*1/7 = 1/10

(randX() - 1)*Y + randY()
（rand7()-1)*7 + rand7()
1 2 3 4 5 6 7 8


扩展：给定一个硬币，向上的概率是p， 如何产生公平事件
抛两次：指定其中一次是正/反， 下一次一定是反/正
