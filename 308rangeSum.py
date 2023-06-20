# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:28:36 2020

@author: liuga
"""
#T[i,j] = T[i-1,j] + T[i, j-1] + matrix[i-1][j-1] - T[i-1][j-1]  O(m*n)
#sum = T[row2][col2] - T[row1-1][col2] - T[row2][col1-1] + T[row1-1][col1-1]
#列之和，(i,j)就是(0,j)+(1,j)+...+(i,j)之和，相当于把很多一维的区间列之和
#sum([x1,y1] [x2,y2]) = presum([x2,y2] - presum[x1-1,y2] - presum[x2,y1-1] + presum[x1-1][y1-1])

class NumMatrix(object):
    obj = NumMatrix(matrix)
    obj.update(row, col, val)
    para2 = obj.e(row1, col1, row2, col2)
    
    def _init_(self, matrix):
        
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col-1]
        self.matrix = matrix
        
    def update(self, row, col, val):
        original = self.marix[row][col]
        if col != 0:
            original -= self.matrix[row][col-1]
        diff = original - val
        
        for y in range(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff
        
    def sumRegion(self, row1, col1, row2, col2):
        region_sum = 0
        for x in range(row1, row2+1):
            region_sum += self.matrix[x][col2]
            if col1 !=0:
                region_sum -= self.matrix[x][col1-1]
        return region_sum
                

#二叉索引树 use dp to compute the prefix sum  lowbit(val) = val & -val
#寻找父结点的方式就是利用lowbit, 也就是一个位置的父结点就是其本身位置 + 其lowbit, 这样就可以在log n的时间更新其父结点的值
#store partial sum in each node. Binary index tree根据数字的二进制表示来对数组中的元素进行逻辑的分层存储
#向上寻找母节点 presum(13) = presum(00001101) = BTT(13) + BTT(12)+ BTT(8) = BTT(1101) + BTT(1100) + BTT(1000)

#二维树状数组
class Solution(object):
    def _init_(self, matrix):
        m = len(matrix)
        if m == 0:
            return        
        n = len(matrix[0])
        if n == 0:
            return
        
        self.matrix = [[0 for j in range(n)] for i in range(m)]
        self.BIT2D = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        m = len(matrix)
        n = len(matrix[0])
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row +1
        while i <= m:
            j = col +1
            while j <= n:
                self.BTT2D[i][j] += diff
                j += (j & (-j))
            i += (i &(-i))

    def getSum(self, row, col):
        ans = 0
        i =  row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                ans += self.BTT2D[i][j]
                j -= (j &(-j))
            i -= (i & (-i))
        return ans

    def regionSum(self, row1, col1, row2, col2)
        return self.getSum(row2, col2) - self.getSum(row2, col1-1)- self.getSum(row1-1,col2) + self.getSum(row1-1, col1-1)
'''   
#n - lowbit(bit)为左祖父/父节点 n + lowbit(bit)为右祖父/父节点 n-lowbit(bit)+1为左子树的底层节点
sum(k) = A[1]+ ....+ A[k] 有BIT后
for(i = k , i >0; i = i - lowbit(i))
    ans ++ BIT[i] #BIT[i]代表nums数组里在i之前的部分元素和
求sum(k)将K以及K的所有左祖父/父节点相加

C[t]展开的项数: lowbit(t)

Binary Indexed Tree的建立非常简单。我们只需初始化一个全为0的数组，并对原数组中的每一个位置对应的数字调用一次update(i, delta)操作即可。这是一个O(nlogn)的建立过程
给定一个长度为n的输入数组list。

1: 初始化长度为n + 1的Binary Indexed Tree数组bit，并将list中的数字对应地放在bit[1]到bit[n]的各个位置。
2: 对于1到n的每一个i，进行如下操作：令j = i + (i & -i)，若j < n + 1，则bit[j] = bit[j] + bit[i]
'''


#PREFIX SUM
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.matrix = matrix
        self._m = [[0] for _ in range(R) ]
        for r in range(R):
            for c in range(C):
                self._m[r].append(self._m[r][-1] + matrix[r][c])
        

    def update(self, row: int, col: int, val: int) -> None:
        real = self.matrix[row][col]
        diff = val - real
        # add diff to all next
        for c in range(col+1, len(self._m[0])):
            self._m[row][c] += diff
        self.matrix[row][col] = val
    
   

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for r in range(row1, row2+1):
            ans += (self._m[r][col2+1] - self._m[r][col1] )
            
        return ans

