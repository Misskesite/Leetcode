# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:26:32 2020

@author: liuga
"""
import collections

class Solution(object):
    def minMutation(self, start, end, bank):
        bfs = collections.deque()
        bfs.append((start,0))  #bfs = [(start,0)]
        bankset= set(bank)
        
        while bfs:
            gene, step = bfs.popleft()
            if gene == end:
                return step
            for i in range(len(gene)):
                for x in "ACGT":
                    newGene = gene[:i] + x + gene[i+1:]
                    if newGene in bankset and newGene != gene:
                        bfs.append((newGene, step+1))
                        bankset.remove(newGene) #重要的一步，避免重复搜索? 先1，后2， 先2 后1
        return -1

                

class Solution2(object):
    def minMutation(self, start, end, bank):
        bankset = set(bank)
        
        if end not in bankset:
            return -1

        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA",
        }
        queue = [(start, 0)]

        while queue:
            gene, step = queue.pop(0)

            if gene == end:
                return step

            for i, s in enumerate(gene):
                for c in change_map[s]:
                    new = gene[:i] + c + gene[i+1:]
                    if new in bankset:
                        queue.append((new, step+1))
                        bankset.remove(new)
        return -1
    
#此法为主？
class Solution2(object):
    def minMutation(self, start, end, bank):
        q = deque()
        q.append((startGene,0))  #bfs = [(start,0)]
        bankset = set(bank)
        if endGene not in bankset:
            return -1
        visited = set()

        while q:
            gene, step = q.popleft()
            visited.add(gene)
            
            for i in range(len(gene)):
                for x in "ACGT":
                    if x != gene[i]:
                        newGene = gene[:i] + x + gene[i+1:]
                        if newGene in bankset and newGene not in visited:
                            if newGene == endGene:
                                return step + 1
                            q.append((newGene, step+1))
                            visited.add(newGene)
        return -1
