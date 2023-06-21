# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:47:33 2020

@author: -
"""

class Solution(object):
    def wordType(self, sentence, rows, cols):
        wcnt = len(sentence)
        wlens = map(len,sentence)
        slen = sum(wlens) + wcnt
        
        dp = dict()
        pr = pc = pw = ans = 0
        while pr < rows:
            if (pc,pw) in dp:
                pr0, ans0 = dp[(pc,pw)]
                loop = (rows- pr0)/(pr-pr0+1)
                ans = ans0 + loop*(ans-ans0)
                pr = pr0 + loop*(pr-pr0)
            else:
                dp[(pc,pw)] = pr,ans
            scount = (cols - pc)/ slen
            ans += scount
            pc += scount*slen + wlens[pw]
            if pc <= cols:
                pw += 1
                pc += 1
                if pw == wcnt:
                    pw = 0
                    ans +=1
                    
            if pc >= cols:
                pc = 0
                pr +=1
        return ans
    
            
            

#直接的方法是每次扫描一行，尝试能放几个，这样时间复杂度会高一点．另外一种方法是把所有的字符串都加起来，然后每次看如果位移一整行的距离是否正好落在这个字符串的空格位置，如果不是的话就退后，直到遇到一个空格．
#start记录的是有效位(effective bit)的个数(原字符串位置a-bcd-e-a-bcd-e-)。我们必须记录有效空位的个数
class Solution2(object):
    def wordType(self, sentence, rows, cols):
        str = ""
        for val in sentence:
            str += val + " "   #a-bcd-e-
            l = len(str)
            start = 0
        for i in range(rows):
            start += cols
            if str[start % l] == " ":
                start += 1
            else:
            #不为空，进入循环，移除不合法的空位
                while start > 0 and str[(start - 1)% l != " ":
                    start -= 1
        return start/l 

#此解法为主
class Solution:
  def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
      combined = ' '.join(sentence) + ' '
      n = len(combined)
      i = 0

      for _ in range(rows):
          i += cols
          if combined[i % n] == ' ': #如果某个单词刚好填满一行时，之后就不用加空格, 看例子3
              i += 1   #算有效空位个数的时候还是要加上这个空格的
          else: #不是空格 
              while i > 0 and combined[(i - 1) % n] != ' ':
                  i -= 1 #减去不必要的空格，比如例子1 -2空格 remove extra zeros(redundant)

      return i // n                                     
                            
'''
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
输出2

Explanation:
a-bcd- 
e-a---
bcd-e-

rows = 2, cols = 8, sentence = ["hello", "world"]
输出1

Explanation:
hello---
world---

rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
输出1

Explanation:
I-had
apple
pie-I
had--
