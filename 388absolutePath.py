# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:25:16 2020

@author: liuga
"""
#使用栈
class Solution(object):
    def lengthpath(self, input):
        stack = [(-1,0)]     #目录深度，当前总的字符串的长度
        max_len = 0
        
        for p in input.split("\n"):
            depth = p.count('\t')
            p = p.replace('\t','')
            while stack and depth <= stack[-1][0]: #当前目录更浅
                stack.pop()
                
            if '.' not in p: #目录
                stack.append((depth, len(p) + stack[-1][1]+1)) #1为反斜杠\
            else:            #文件
                max_len =  max(max_len, len(p)+ stack[-1][1])
                
        return max_len

class Solution2(object):
    def lengthLongestpath(self, input: str) -> int:
        res = 0
        depth_lenth_map = {-1: 0}  #保留每层路径的长度
        for line in input.split("\n"):
            depth = line.count('\t') #判断第几层
            depth_lenth_map[depth] = depth_lenth_map[depth-1] + len(line)- depth
            if line.count('.'):
                #每层都要添加depth个
                res = max(res, depth_lenth_map[depth] + depth)
        return res

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        dict={}
        longest=0
        fileList=input.split("\n")
        for i in fileList:
            if "." not in i:  #是文件夹
                key = i.count("\t") #是几级文件夹
                value = len(i.replace("\t","")) #除去\t后的长度，是实际长度
                dict[key]=value
            else: #是文件。
                key=i.count("\t")
                #　文件的长度：所有目录的长度＋文件的长度＋“\”的数量
                length = sum([dict[j] for j in dict.keys() if j<key]) + len(i.replace("\t","")) + key
                longest=max(longest,length)
        return longest

    
def lengthLongestPath(self, input):
    maxlen = 0
    pathlen = {0: 0}
    for line in input.splitlines():
        name = line.lstrip('\t')
        depth = len(line) - len(name) #/t个数？
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
    return maxlen
