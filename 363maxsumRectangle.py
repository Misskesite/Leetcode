# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:12:45 2020

@author: liuga
"""
import bisect

class Solution(object):
    def maxsumRectangle(self, matrix,k):
        
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        
        M = max(m,n)
        N = min(m,n)
        
        ans = None
        for x in range(N):
            sums = [0]*M
            for y in range(x,N):
                slist, num = [],0
                for z in range(M):
                    sums[z] += matrix[z][y] if m > n else matrix[y][z]
                    num += sums[z]
                    if num <= k:
                        ans = max(ans, num)
                    i = bisect.bisect_left(slist, num-k)
                    if i != len(slist):
                        ans = max(ans, num- slist[i])
                    bisect.insort(slist,num)
        return ans or 0
                        
            
#the problem reduces to finding  i,j  such that  i < j  and  cum[j] − cum[i] is as close to  k  but lower than it.( accumulate the sum of each row between columns i and j) scan from left to right and put the cum[i] into a set
#when you process the cum[j], what you need to retrive from the set is the smallest number in the set, which is bigger than cum[j] - k (大于cum[j] - k 的最小值)
#利用前缀和，把每行的总和求得，通过前缀和找差值最大就能找到最大矩阵
import bisect
class Solution2(object):
    def maxsumSubmatrix(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        res = float("-inf")
        for left in range(col): #一列一列扫，扫完一列，从第二列开始扫
            #left为左边界，每行的总和
            sums = [0]*row      #对每一列，往下一行行扫
            for right in range(left, col):
                for j in range(row):
                    sums[j] += martix[j][right]
                    #在left, right边界下的矩阵，求不超过k的最大数值和
                    
                arr = [0]
                cur = 0
                for tmp in sums:
                    cur += tmp
                    #二分法 寻找小于等于 cur-k的index
                    i = bisect.bisect_left(arr, cur - k)
                    if i < len(arr):
                        res = max(res, cur - arr[i])
                    bisect.insort(arr, cur)
        return res
                    
        
'''
Iterating index i from left to right.
Calculate prefixSum so far, let name it right
Try to find the left prefixSum so that right - left <= k => left >= right - k.
We can use BST to find the least key greater than or equal to the given x. So left = bst.ceiling(right-k).
If we found a valid left, then we update the answer by ans = max(ans, right - left).
Then we try all possible pairs of (r1, r2) of rows in the matrix, where 0 <= r1 <= r2 < m. Make an array of n integer, where arr[c] = sum(matrix[r1][c]...matrix[r2][c]), then solve that sub problem.


bisect.bisect_left([1,3,5], 2)
Out[8]: 1

bisect.bisect_right([1,3,5], 2)
Out[20]: 1

bisect.bisect_left([1,3,4], 4)
Out[9]: 2

bisect.bisect_left([1,3,4], 5)
Out[10]: 3

bisect.bisect_right([1,3,5], 3)
Out[21]: 2

bisect.bisect_left([1,3,5], 3)
Out[23]: 1

bisect.bisect_right([1,3,5], 5)
Out[24]: 3
