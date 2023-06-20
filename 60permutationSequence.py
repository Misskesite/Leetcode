# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:31:59 2019

@author: liuga
"""
#计算k中有几个(n-1)!就可以确定首位的数字
class Solution(object):
    def permutationSequence(self, n, k):
        ans = ''
        fact = [1]*n
        num = [str[i] for i in range(1,10)]
        for i in range(1,n):
            fact[i] = fact[i-1]*i
            
        k -= 1    #下标从0开始         
        for i in range(n, 0, -1): #i从n到1
            first = k // fact[i-1]
            k %= fact[i-1]
            ans += num[first]
            num.pop(first)
        return ans

#For permutations of n, n groups, the first digit start with 1 with (n-1)! permutations formed by rest of digits, next (n-1)! ones start with 2, ... and so on. And in each group of (n-1)! permutations, the first (n-2)! permutations start with the smallest remaining number
#for n numbers the permutations can be divided to (n-1)! groups, for n-1 numbers can be divided to (n-2)! groups。  Each 1st digit is "attached" to (n-1)! =2! = 2 permutations formed by rest of digits.
#, to choose 1st digit, simply calculate (k-1) / (n-1)! and use it to index into an array of digits [1,2,3,] Once 1st digit is chosen, we choose 2nd and so on recursively.


Idea:

For an n-element permutation, there are (n-1)! permutations started with '1', (n-1)! permutations started with '2', and so forth. Therefore we can determine the value of the first element.

After determining the first element, there are (n-1) candidates left. Then there are (n-2)! permutations started with the minimum element within the remaining set, and so forth.

class Solution(object):
    def getPermutation(self, n, k):
        used = [[False] for _ in range(n+1)]
        fabo = [1]*(n+1)
        for i in range(1, n):
            fabo[i] = fabo[i-1]*i

        path = []
        dfs(0, path)

        def dfs(index, path):
            if index == n:
                return
            count = fabo[n-index-1]  //#第一次进入的是n-1
            for i in range(1, n+1):
                if used[i]:
                    continue

                if count < k:
                    k -= count
                    continue

                path.append(i)
                used[i] = True
                dfs(index+1, path)  //直接定位到第K个排列，不需要回溯，即不需要重置状态
                return              //没必要搜索下去，直接返回
            
