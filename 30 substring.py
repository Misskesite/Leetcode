# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:46:37 2019

@author: liuga
"""

class Solution:
    def findSubsring(self, S, L):
        ans=[]
        Dict = dict.fromkeys(L, 0)
        for word in L:
            Dict[word] = Dict[word]+1
        
        totWord = len(L)
        wordLen = len(L[0])
        slen = len[S]- totWord*wordLen
        
        for i in range(0, slen+1):
            cnt = dict.fromkeys(L,0)
            okNum =0
            for k in range(0, totWord):
                cur = S[i + k*wordLen: i + (k+1)*wordLen]
                if (cur in Dict):
                    cnt[cur]= cnt[cur]+1
                    
                    if(cnt[cur] > Dict[cur]):
                        break
                okNum = okNum +1
                
                if(okNum == totWord):
                    ans.append(i)
                
        return ans


class Solution:
  def findSubstring(self, s: str, words: List[str]) -> List[int]:
       if len(s) == 0 or words == []:
           return []

        k = len(words)
        n = len(words[0])
        ans = []
        count = Counter(words)

        for i in range(len(s) - k * n + 1):
            seen = defaultdict(int)
            j = 0
            while j < k:
                word = s[i + j * n: i + j * n + n]
                seen[word] += 1
                if seen[word] > count[word]:#出现不存在或者多出了个个数的单词？
                    break
                 j += 1
            if j == k:
                ans.append(i)

          return ans
            
#s的长度为n, words里面有m个单词 时间复杂度O(m*n) 空间复杂度O(m)
from collections import defaultdict
class Solution2(object):
    def findString(self, s, words):
        s_len = len(s)
        word_len = len(words[0])
        word_num = len(words)
        
        res = []
        
        words_dict = defaultdict()
        
        for word in words:
            words_dict[word] += 1
           
                
        #//遍历所有子串        
        for i in range(s_len - word_len*word_num + 1):
            j = 0
            cur_dict = dict.fromkeys(words,0)       #fromkeys创建一个新字典,值为0？
            #或者 cur_dict = {}
            while j < word_num:
                cur = s[i + word_len*j : i + word_len*(j+1)] 
                if cur not in words_dict: #出现不存在的单词
                    break
                if cur in cur_dict:                    
                    cur_dict[cur] += 1
                
                if cur_dict[cur] > words_dict[cur]: #某个单词大于所需，结束此区间。保证cur_dict[cur] <= words_dict[cur]
                    break
                j += 1  #单词数加一
            
           if j == word_num:  #n个窗口都匹配成功
               res.append(i)
            
        return res

#滑动窗口              
from collections import Counter
class Solution3(object):
    def findString(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_num = len(words)

        words_dict = Counter(words)

        res = []

        for i in range(word_len):
            cur_cnt = 0
            l = i
            r = i
            cur_Counter = Counter()
            while right + word_len <= n :
                w = s[r: r + word_len]
                r += word_len
                cur_Counter[w] += 1
                cur_cnt += 1
                while cur_Counter[w] > words[w]:
                    left_w = s[l: l + word_len]
                    l += word_len
                    cur_Counter[w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num:
                    res.append(l)
        return res
                
            
        
