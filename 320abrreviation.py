
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:01:28 2020

@author: liuga
"""
#every char has 2 choice: abbreviate or keep.
class Solution(object):
    def abbreviation(self, word):
        res = []
        def dfs(res, word, str):
            if len(word) == 0:
                return res.append(str)
            
            self.dfs(res, word[1:], str+ word[:1])
            
            for i in range(1, len(word)):
                dfs(res,word[:i+1], str+ "i" + word[i])
                
            self.dfs(res, "", str + len(word))  
            
        dfs(res, word, '')
        
        return res
            
            
#递归法 O(2**n)
class Solution2(object):
    def generateAbbreviate(self, word):
        res = []
        
        def helper(i, tmp, cnt):
            #cnt代表前面记录了多少数字
            if i == len(word):
                if cnt > 0:            #cnt为0时不能拼接
                    tmp = tmp + str(cnt)
                res.append(tmp)
                return 
            else:
                #不用word[i]
                helper(i+1, tmp, cnt+1) #累加已经省略的数字+1
                #用word[i]
                helper(i+1, tmp + (str(cnt) if cnt > 0 else "") + word[i], 0) #省略掉的字符从0开始
        helper(0, "", 0)
        return res
        

class Solution:
  def generateAbbreviations(self, word: str) -> List[str]:
    ans = []

    def getCountString(count: int) -> str:
      return str(count) if count > 0 else ''

    def dfs(i: int, count: int, path: List[str]) -> None:
      if i == len(word):
        ans.append(''.join(path) + (str(cnt) if cnt > 0 else '')
        return

      # Abbreviate word[i]
      dfs(i + 1, count + 1, path)
      # Keep word[i], so consume the count as a string
      path.append((str(count) if count > 0 else '') + word[i])
      dfs(i + 1, 0, path)  # Reset count to 0
      path.pop()
      #dfs(i + 1, 0, path + [str(count) if count > 0 else [])] + word[i] ) ?简写

    dfs(0, 0, [])
    return ans
    
#和全排列，子集不一样。构造字符缩写的起点，顺序不能变
''' 每一步，选和不选
Round1 [W, 1]
Round2 [WO ,W1 ,1O, 2]
Round3 [WOR, WO1, W1R, W2. 1OR, 1O1, 2R, 3]
Round4 [WORD, WOR1, WO1D, WO2. W1RD, W1R1,W2D, W3. 1ORD, 1OR1,1O1D, 1O2,2RD, 2R1, 3D,4]
                    
        
