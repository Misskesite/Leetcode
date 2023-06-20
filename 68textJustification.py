# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:41:30 2019

@author: liuga
"""

class Solution(object):
    def textjustify(self, words, maxwidth):
         start = end = 0
         result = []
         cur_words_len = 0
         
         for i, word in enumerate(words):
             if len(word) + cur_words_len + end - start > maxwidth:
                 if end - start == 1:
                     result.append(words[start] + ''*(maxwidth-cur_words_len))
                 else:
                     total_space = maxwidth-cur_words_len
                     space, extra = divmod(total_space, end-start-1)
                     
                     for j in range(extra):
                         result.append(''*space).join(words[start:end])
                         
                     
                 cur_words_len = 0
                 start = end = i
             end += 1
             curr_words_len += len(word)
            
         result.append(''.join(words[start:end]) + '' * (maxwidth - cur_words_len - (end - start - 1))
         return result


#累加长度，用一个列表保存当前的单词，长度超过时分两种情况:一个单词，多个单词(避免除以0)
#最后一行有2种情况: 正好填满maxWidth时和其它行处理相同，有多余空格时放在循环外单独处理
#知道一行的所有n个words，以及总长curLen之后要决定空格分配：
#平均空格数：k = (L - curLen) / (n-1)
class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        line = []
        length = 0
        for word in words:
            if len(word) + length > maxWidth:
                space = maxWidth - lenth -1
                if len(line)> 1:
                    gap = len(line)-1
                    i = spaces//gaps +1
                    j = spaces%gaps
                    t = ""
                    for k in range(len(line)):
                       t += line[k]
                       if k < len(line)-1:
                           t += " "*i
                       if k < j:
                       t += ""
                else:
                    t = line[0] + spaces*" "
                res.append(t)
                length = 0
                line = []
            length += len(word) +1
            line.append(word)

        #last line
        if line:
            t = ""
            for word in line:
                t += word + " "
            t += " "*maxWidth
            t = t[:maxWidth]
            res.append(t)
        return res

#此写法为主
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        row = []
        rowLetters = 0

        for word in words:
            if rowLetters + len(word) + len(row) > maxWidth:
                for i in range(maxWidth - rowLetters):  #spaces?
                    row[i % (len(row) - 1 or 1)] += ' ' # or 1 is for deal with len(row)= 1
                ans.append(''.join(row))
                row = []
                rowLetters = 0
            row.append(word)
            rowLetters += len(word)

        return ans + [' '.join(row).ljust(maxWidth)]

#改写
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        row = []
        rowLetters = 0

        for word in words:
            if rowLetters + len(word) + len(row) > maxWidth: #evey word math a space?
                spaces = maxWidth - rowLetters
                if len(row) == 1:
                    row[0] += ' '*spaces
                else:
                    space = spaces// (len(row) - 1)
                    left = spaces %(len(row) - 1)
                    if left > 0:
                        for i in range(left):
                            row[i] += ' ' 
                        
                    for i in range(len(row)-1):
                        row[i] += ' '*(space)
                '''
                    for k in range(ceil(spaces/(len(row)-1))):
                        for i in range(len(row)-1):
                            row[i] += " "
                            spaces -= 1
                            if spaces == 0:
                                break
                '''

                ans.append(''.join(row))
                row = []
                rowLetters = 0
            row.append(word) #not larger than maxWidth, add word
            rowLetters += len(word) # update rowLetter

        return ans + [' '.join(row).ljust(maxWidth)] #for the last line                     
