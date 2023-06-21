# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:07:32 2020

@author: liuga
"""
#找到D的位置和长度，转置？
class Solution(object):
    def findpermutation(self,s):
        size = len(s)
        nums = list(range(1,size+2))
        ans = []
        idx = 0
        while idx < size:
            if s[idx] == 'D':
                cnt = 0
                while idx < size and s[idx] != 'I':
                    idx +=1
                    cnt +=1
                ans += nums[:cnt+1][::-1]
                nums = nums[cnt+1:]
                if idx < size:
                    idx +=1
            else:
                ans += [nums[0]]
                nums = nums[1:]
                idx +=1
        return ans+nums
            

#单调栈
class Solution(object):
    def findPermutation(self, s):
        n = len(s)
        res = [0]*(n+1)
        stack = []
        j = 0

        for i in range(1, n+1):
            if s[i-1] == "I":
                stack.append(i)
                while stack:
                    j += 1
                    res[j] = stack.pop()
            else:
                stack.append(i)

        stack.append(n+1)
        while stack:
            j += 1
            res[j] = stack.pop()
            
        return res
            


class Solution:
  def findPermutation(self, s: str) -> List[int]:
    ans = []
    stack = []

    for i, c in enumerate(s):
      stack.append(i + 1)
      if c == 'I':
        while stack:  # Consume all decreasings
          ans.append(stack.pop())
    stack.append(len(s) + 1)

    while stack:
      ans.append(stack.pop())

    return ans
        
        ans, stack = [], []
        for i, ch in enumerate(s + "I"): 
            if ch == "D": stack.append(i+1)
            else: 
                ans.append(i+1)
                while stack: ans.append(stack.pop())
        return ans 
