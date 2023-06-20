# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:19:35 2020

@author: liuga
"""
#backtracking + trimming
class Solution(object):
    def isActivenumber(self, num):
        if len(num)< 3:
            return False
        if len(num) == 3 :
            return int(num[:1]) + int(num[1:2]) == int(num[2:])
        
        return self.dfs(num,[])
    
    #数字不以0开头，单独的0是允许的
    def dfs(self, num_str, path):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
            return False
        if not num_str and len(path) >= 3:
            return True
        
        for i in range(len(num_str)):
            cur = num_str[:i+1]
            if cur[0] == '0' and len(cur) != 1:
                continue
            if self.dfs(num_str[i+1:], path + [int(cur)]):
                return True
        return False
    


class Solution(object):
    # According to:
    # https://leetcode.com/discuss/70089/python-solution
    # The key point is choose first two number then recursively check.
    # DFS: recursice implement.
    def isAdditiveNumber(self, num):
        length = len(num)
        for i in range(1, length/2+1):
            for j in range(1, (length-i)/2 + 1):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if self.isValid(first, second, others):
                    return True
        return False

    def isValid(self, first, second, others):
        # Numbers in the additive sequence cannot have leading zeros,
        if ((len(first) > 1 and first[0] == "0") or (len(second) > 1 and second[0] == "0")):
            return False
        sum_str = str(int(first) + int(second))
        if sum_str == others:
            return True
        elif others.startswith(sum_str):
            return self.isValid(second, sum_str, others[len(sum_str):])
        else:
            return False
