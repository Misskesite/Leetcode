# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:58:52 2019

@author: liuga
"""

class Solution(object):
     def digit2Letters{
             '2':"abc",
             '3':"def",
             '4':"ghi",
             '5':"jkl",
             '7': "pqrs",
             '8': "tuv",
             '9': "wxyz",             
             }:

     def letterCombination(self, digits):
         if not digits:
             return []
         result = []
         self.dfs(digits, "", result)
         return result
     
        def dfs(self, digits, current, result):
            if not digits:
                result.append(current)
                return
            for c in self.digit2Letters(digits[0]):
                self.dfs(digits[1:], current + c, result)

#回溯
class Solution(object):
     def letterCombinations(self, digits):
          if not digits:
               return []
          phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
          }
          
          res = []
          combination = []
          def backTrack(index, combination):
               if index == len(digits):
                    res.append("".join(combination))
               else:
                    digit = digits[index]
                    for letter in phoneMap[digit]:
                         backTrack(index+1, combination + [letter])
          backTrack(0, combination)
          return res
          
          
#队列 O(3**M 4**N) M是3个字母的数字个数 N是4个字母的数字个数
class Solution(object):
     def letterCombination(self, digits):
          if not digits:
               return []
          phone = ['abc', 'def', 'ghi', 'mno', 'pqrs', 'tuv','wxyz']
          queue = [''] #初始化队列
          for digit in digits:
               for _ in range(len(queue)):
                    tmp = queue.pop(0)
                    for letter in phone[ord[digit] - 50] #不使用int转字符串，使用 Ascii码
                         queue.append(tmp + letter)
          return queue
