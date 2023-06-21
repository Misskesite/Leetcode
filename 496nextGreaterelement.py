# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:28:47 2020

@author: liuga
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        answer = []
        for num1 in findNums:
            index = -1
            for i, num2 in enumerate(nums):
                if num1 == nums[i]:
                    index = i
                    break
            while index < len(nums) and num1 >= nums[index]:
                index +=1
            if index == len(nums):
                answer.append(-1)
            else:
                answer.append(nums[index])
            
        return answer
        
#单调栈 O(n)
class Solution2(object):
    def nextGreaterElement(self, nums1, nums2):
        dic, stack = {}, []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dic[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        return [dic.get(x, -1) for x in nums1]


class Solution3:
    def nextGreaterElement(self, nums1, nums2):
        dic, stack = {}, []

        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack: 
                dic[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        return [dic.get(x, -1) for x in nums1]
    

#类似方法2
class Solution4:
    def nextGreaterElement(self, nums1, nums2):
        stack, hashmap = list(), dict()
        for n in nums2:
            while len(stack) != 0 and stack[-1] < n:
                hashmap[stack.pop()] = n
            stack.append(n)
        return [hashmap.get(n,-1) for n in nums1]



