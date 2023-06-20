# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:10:21 2019

@author: liuga
"""
#类似于77, 本题K 固定了树的深度
class Solution(object):
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(k: int, n: int, s: int, path: List[int]) -> None:
            if k < 0 or n < 0:
                return
            
            if k == 0 and n == 0:
                ans.append(path)
                return
            

            for i in range(s, 10): #(s, 9-(k-len(path))+2)
                dfs(k - 1, n - i, i + 1, path + [i])

        dfs(k, n, 1, [])
        return ans


class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        self.dfs(list(range(1, 10)), k, n, [], res)
        return ret
    
    def dfs(self, nums, k, n, path, ret):
        if k < 0 or n < 0:
            return 
        if k == 0 and n == 0:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], res)
            
    
#递归三部曲  1 确定递归函数参数 2 确定终止条件(path长度和k相同，sum=targetsum,不同直接返回) 3 单层搜索过程(剪枝)
class Solution2(object):
    def combinationSum(self, k, n):
        res = []
        path = []
        #targetsum 目标和，即n. sum为path中元素总和，
        def backtracking(targetSum, k, cursum, index):
            if cursum > targetSum: #剪枝
                return

            if len(path) == k and cursum == targetSum:
                res.append(path)
                return
            #numsMax = n - (1 + k - 1)*(k - 1)/2
            #for i in range(index, min(numMax, 9) + 1)
            for i in range(index, 9 - (k - len(path))+2): #剪枝优化
                path.append(i)
                cursum += i
                backtracking(targetSum, k, cursum, i+1)
                cursum -= i #回溯
                path.pop()

        backtracking(n, k, 0 ,1)
        return res
            
#Python中一切皆对象，所有的变量都是对象的引用
#对一个变量赋值，并不会改变变量引用的对象，而是使这个变量指向了另一个对象
a = [1]
a.append(2)  # 这样不会改变a的引用
a = a + [2]  # 这样实际上是产生了一个新的list对象，并将a指向新的对象
