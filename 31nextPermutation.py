# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:42:00 2019

@author: liuga
"""
#下一个字典序更大的排列， 从后向前找第一个相邻升序数列对,尽可能靠右的低位交换。增加的幅度尽可能小(尽可能小的大数与前面的小数交换)

#123465 交换 5，4 得到123564，将5后面的数字重置为升序，即 123546，它比123564更小
class Solution(object):
    def nextPermutation(self, nums):
        length = len(nums)
        
        Tindex = 0
        Cindex = 0
        
        for i in range(length-1, 0, -1):
            if nums[i] > nums[i-1]:
               Tindex = i-1 #left? 对应4
               break
           
        for i in range(length-1, -1, -1): #从后向前查找
            if nums[i] > nums[Tindex]:
               Cindex = i   #right? 对应5
               break
           
        nums[Tindex], nums[Cindex] = nums[Cindex],nums[Tindex]
            
        if Tindex == Cindex == 0:
            nums.reverse() #654321 没有更大的，直接变成123456
                
        else:
            nums[Tindex+1:] = reversed(nums[Tindex+1:] 
                
          
                                       
                                       
