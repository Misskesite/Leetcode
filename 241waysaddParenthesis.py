# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:23:27 2020

@author: liuga
"""
import re
class Solution(object):
    def parentheses(self, input):
        
        dic = dict()
        nums =[]
        ops = []
        input = re.split(r'(\D)',input)
        for x in input:
            if x.isdigit():
                nums.append(x)
            else:
                ops.append(x)
        self.dfs(nums, ops, dic)
        return dic.values()
        
    def dfs(self, nums, ops, dic):
        if ops:
            for x in range(len(ops)):
                self.dfs(nums[:x] + ['('+ nums[x] + ops[x] + nums[x+1] + ')'] + nums[x+2:], ops[:x] + ops[x+1:], dic)
        elif nums[0] not in dic:
            dic[nums[0]] = eval(nums[0])
            
            
#分治法,递归求子函数的解 加 @lru_cache(None)
class Solution2(object):
    def diffWaysCompute(self, input):
        if input.isdigit():
            return [int(input)]
        ''''
        加 memo = dict()
        if input in memo:
            return mmeo[input]
        '''
        
        res = []
        for i, char in enumerate(input):
            if char in ['+','-','*']:
                left = self.diffWaysCompute(input[:i])
                right = self.diffWaysCompute(input[i+1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left: #left, right是计算出的值列表(括号里面再加括号有多种情况)
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        if not res: #没有加运算符，里面是单独的数
            res.append(int(input))
        #memo[input] = res
        return res


    
