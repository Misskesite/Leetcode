# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:22:50 2020

@author: liuga
"""
#DFS  Time complexity: O(n^2*3^n), space complexity: O(n^2*3^n)
class Solution(object):
    def expression(self, nums, target):
        if len(nums) == 0:
            return 
        self.res = []
        self.dfs(nums, -target, "", 0, 0, 1)
        return self.res
        
    def dfs(self, nums, sum, path, pos, pre, val):
        pre = pre*10 + nums[pos] - '0'
        if pre > float('inf'):
            return
        if sum + pre*val== 0 and pos == len(nums)-1:
            self.res.append(path + nums[pos])
            
        if pos == len(nums) - 1:
            return
        if pre: #pre是前面累计下来的值，val表示前面是什么运算，1为加，1-为减，乘需要累计乘积
            self.dfs(nums, sum, path + nums[pos], pos+1, pre, val)
        self.dfs(nums, sum + pre*val, path + nums[pos]+ '+', pos + 1, 0,  1)
        self.dfs(nums, sum + pre*val, path + nums[pos]+ '+', pos + 1, 0, -1)
        self.dfs(nums, sum, path + nums[pos] + '*', pos + 1, 0, pre*val)



#dfs 0作为一位是允许的，多位且首部为0是不被允许的  nums = 1 0 5 target = 5
#字符串长度为n，每个位置四个决策(不插入，+，-，*)共有n-1个位置需要决策，对所有的表达式执行复杂度为O(n) 整体复杂度O(n*4(n-1))
class Solution(object):
    def expression(self, nums, target):
        if len(nums) == 0:
            return
        ans = []
        n = len(nums)

        def dfs(idx, pre, cur, s): #prev上一次的操作数？
            if idx == n:
                if cur == target:
                    ans.append(s)
                    return

            val = 0
            #先保存路径，将当前运算符记录下来
            for i in range(idx, n):
                if i != idx and nums[idx] == "0":
                    break
                val = val * 10 + int(nums[i]) #截取[idx:i+1]   
                if idx == 0:                   #表达式开头不能添加符号
                    dfs(i + 1, val, val, str(val))
                else:
                    dfs(i + 1, pre*val, cur - pre + pre*val, s + "*" + str(val))
                    dfs(i + 1, val, cur + val, s + "+" + str(val))
                    dfs(i + 1, -val, cur - val, s + "-" + str(val))
                    
        dfs(0 ,0 ,0 , "")
        return ans

    
#num = "232", target = 8  输出: ["2*3+2", "2+3*2"] num数字可能为0
def addOperators(self, num, target):
    res, self.target = [], target
    for i in range(1,len(num)+1):
        if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
            self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
    return res

def dfs(self, num, temp, cur, last, res):
    if not num:
        if cur == self.target:
            res.append(temp)
        return
    for i in range(1, len(num)+1):
        val = num[:i]
        if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
            self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
            self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
            self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)
