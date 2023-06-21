# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:09:45 2020

@author: liuga
"""
#类似于416 backtracing 一个数字分四组，每组的和相同
class Solution(object):
    def matchSquare(self, nums):
        
        if not nums or len(nums) <4:
            return False
        s = sum(nums)
        div, mod = divmod(s, 4)
        if mod !=0 or max(nums)> s/4:
            return False
        nums.sort(reverse = True) #排序后，跳过向同的边        
        target = [div]*4
        return self.dfs(nums, 0, target)
    
    def dfs(self, nums, index, target):
        
        if index == len(nums):
            #可以加 判断四条边最后都相等，火柴用完肯定四条边相等
            return True
        num = nums[index]
        for i in range(4):
            #重复去除 如果target[i]和target[i-1] 上一个分支和现在的一样，上个分支没有成功，这个也一样
            if target[i] > num:
                target[i] -= num
                if self.dfs(nums,index+1,target):
                    return True
                target[i] += num #当前火柴放在target[i]边上 不能构成正方形
        
        return False

#前面数组比较小，这会导致递归的比较深，所以我们可以先对数组进行排序，从大的开始递归
#时间复杂度O(2**n)
class Solution2(object):
    def matchSquare(self, nums):
        if not nums or len(nums) < 4:
            return False
        s = sum(nums)
        div = s//4
        if s % 4 != 0:
            return False

        nums.sort(reverse = True)
        

        sides = [0]*4
        
        def dfs(i):
            if i == len(nums):
                return True
            for j in range(4): #四条边对称，从第一条边放，如果成功就返回
                if sides[j] + nums[i] <= div:
                    #需要去重 剪枝 如果两个sums值相同，那么把数字放在两个桶效果一样, 如果上一个放入失败，回溯到原始值sums[j-1]
                    if j > 0 and sides[j] == sides[j-1]: #加剪枝，速度提高更快
                        continue
                    sides[j] += nums[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= nums[i]
            return False

        return dfs(0)
        
        
        


#继续优化，四条边没有区别，如果先遍历一条边
