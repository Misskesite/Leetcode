# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:54:09 2020

@author: liuga
"""
import collections
#差一个字符保留原样，因为它们的缩写也冲突， 差两个字符的可以缩写(前缀不同)
class Solution(object):
    def abbr(self, word, size):
        if len(word) - size <= 3:
            return word
        return word[:size+1]+ str(len(word)-size-2)+ word[-1]
    
    def solve(self, dict, size):
        dlist = collections.defaultdict(list)
        for word in dict:
            dlist[self.abbr(word,size)].append(word)
        for abbr, wlist in dlist.items(): #python3里面没有iteritems()
            if len(wlist)== 1:
                self.dmap[wlist[0]] = abbr #wlist[0]为前缀长度为1?
            else:
                self.solve(wlist, size+1) #增加前缀长度，直到没有冲突
        
    def wordAbbriviaion(self, dict):
        self.dmap = {}
        self.solve(dict, 0)
        return list(map(self.dmap.get, dict)) #获取dmap的值列表 类似于迭代生成dmap.get(dict)

#此解法为主
class Solution(object):
    def abbr(self, word, size):
        class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        
        def solve( words, size):
            //Dictionary contains abbrevation to words list
            dlist = defaultdict(list)
            for word in words:
                // If length can not be decreased by breaking, add the word to answer
                if size >= len(word) -  2:
                    self.dmap[word]= word
                    continue
                abbr = word[:size]+ str(len(word)-size-1)+ word[-1]
                dlist[abbr].append(word)
            // Go through the dictionary, if more than 1 word match to same key, break those words with longer prefix
            for abbr, wlist in dlist.items(): 
                if len(wlist)== 1:
                    self.dmap[wlist[0]] = abbr #只有一个match
                else:
                    solve(wlist, size+1) #增加前缀长度，直到没有冲突
            
        
        self.dmap = {}
        solve(words, 1)
        return [self.dmap[word] for word in words] #获取dmap的值列表 类似于迭代生成dmap.get(dict)

  
'''
python2 ?
items()返回的是列表对象，而iteritems()返回的是iterator对象
print dic.items()        #[('a', 'hello'), ('c', 'you'), ('b', 'how')]

print dic.iteritems()   #<dictionary-itemiterator object at 0x020E9A50>

深究：iteritor是迭代器的意思，一次返回一个数据项，直到没有为止

for i in dic.iteritems():
　　 print i
结果：('a', 'hello')
     ('c', 'you')
     ('b', 'how')
'''

#迭代方法?
class Solution2(object):
    def wordAbbriviaion(self, dict):
        
        def makeAbbr(self, word, size == 0):
            if len(word) - size <= 3:
                return word
            return word[:size+1]+ str(len(word)-size-2)+ word[-1]

        ans = []
        n = len(dict)
        prefix = [0]*n

        for word in dict:
            ans.append(makeAbbr(word))

        for i in range(n):
            while True:
                dup_list = []
                for j in range(i+1, n):
                    if ans[j] == ans[i]:
                        dup_list.append(j)

                if not dup_list: #没有冲突？
                    break

                dup_list.append(i)

                for k in dup_list:
                    prefix[k] += 1
                    ans[k] = makeAbbr[dict[k], prefix[k]]
        return ans
    
            
'''       
 对于map, python2返回迭代对象 python3返回list
 map(function, iterable)
