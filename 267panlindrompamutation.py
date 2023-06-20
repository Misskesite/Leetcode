# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 12:54:46 2020

@author: liuga
"""
#"aabb" -> ["abba", "baab"]

#此解法为主
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
         # get character occurrence
        count = Counter(s)
        candidates = ""
        mid = ""
        cnt = 0

        # get mid and candidates characters
        for key, value in count.items():
            if value & 1:
                mid += key
                cnt += 1
            candidates += key * (value // 2)
        
        # can't form any palindrome
        if cnt > 1:
            return []

        ans = []
        # generate all unique palindromes from candidates
        def dfs(candidates, path):
            if not candidates:
                ans.append(path + mid + path[::-1]) #ans.append(''.join(path) + mid + ''.join(path[::-1])) 如果path is []
                return

            for i in range(len(candidates)):                
                if i > 0 and candidates[i] == candidates[i - 1] :
                    continue            
                dfs(candidates[:i] + candidates[i+1:], path + candidates[i])
               

        # backtracking to generate our ans (strings)
        dfs(candidates, "") #[]
        return ans




import collections

class Solution(object):
    def panlindromPumutation(self,s):
        if not s or not self.checkpanlindrom(s):
            return []
        if len(set(s)) == 1:
            return [s]
        
        dic = collections.Counter(s)
        
        news = ""    #去掉可能出现的单独字母后的字符串
        special = "" #可能出现的单独字母, special的个数不能超过1
        for key, val in dic.items():
            if val % 2:
                special = key  # 找到了这个单独的字母
                val -= 1
            news += key * (val // 2)
            
        res = set()
        
        def permutations(word, tmp):
            if not word:
                res.add(tmp + special + tmp[::-1]) #直接去重
            
            for i, char in enumerate(word):
                permutations(word[:i] + word[i + 1:], tmp + char)
                
        permutations(news, "")
        return list(res)


            
    def checkpanlindrom(self, s):
        count = collections.Counter(s)
        flag = 0
        for key, value in count.items():
            if value % 2:
                if not flag:
                    flag = 1
                else:
                    return False
        return True
    
#对偶数个字符全排列？
class Solution:
  def generatePalindromes(self, s: str) -> List[str]:
      # get character occurrence
      count = Counter(s)

      # count odd one
      odd = sum(value & 1 for value in count.values())

      # can't form any palindrome
      if odd > 1:
          return []

      ans = []
      candidates = []
      mid = ''

      # get mid and candidates characters
      for key, value in count.items():
          if value & 1:
              mid += key
      for _ in range(value // 2):
          candidates.append(key)

    # generate all unique palindromes from candidates
    def dfs(used: List[bool], path: List[chr]) -> None:
        if len(path) == len(candidates):
            ans.append(''.join(path) + mid + ''.join(path[::-1]))
            return

        for i, candidate in enumerate(candidates):
            if used[i]:
                continue
            if i > 0 and candidate == candidates[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(candidate)
            dfs(used, path)
            path.pop()
            used[i] = False

    # backtracking to generate our ans (strings)
    dfs([False] * len(candidates), [])
    return ans
