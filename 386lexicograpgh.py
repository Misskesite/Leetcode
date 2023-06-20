# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:27:52 2020

@author: liuga
"""
#类似于440
#迭代 num反应每一层的递归状态，比如123, 当前遍历到3，上一层遍历到2，再上一层遍历到1 要返回上一层，令num //= 10
class Solution(object):
    def lexicograpgh(self, n):
        cur = 1
        ans = []
        for i in range(n):
            ans.append(cur)
            if cur*10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur % 10 == 0: #加1末尾形成0 需要去掉
                    cur //= 10
        return ans
#重写 迭代 
    def lexicalOrder(self, n):
        ans = []
        num = 1
        while len(ans) < n :
            while num <= n: #不断进入下一层
                ans.append(num)
                num *= 10
            while num %10 == 9 or num > n: #不断返回上一层
                num //= 10

            num += 1 #遍历该层的下一个数
        return ans
                
                
    
                    
                
#深度优先 h位的所有数看成h层的k叉树, [1,n]范围的所有整数的字典序就是k叉树的先序遍历顺序
#n = 13 输出:[1,10,11,12,13,2,3,4,5,6,7,8,9]
class Solution(object):
    def lexicalOrder(self, n):
        def dfs(num):
            if num > n:
                return
            ans.append(num)
            for x in range(num*10, num*10 + 10):
                dfs(x)

        ans = []
        for num in range(1, 10):
            dfs(num)
        return ans
                
