# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:11:24 2019

@author: liuga
"""
#To create the max number from num1 and nums2 with k elements, we assume the final result combined by i numbers (denotes as left) from num1 and j numbers (denotes as right) from nums2, where i+j==k.
#Obviously, left and right must be the maximum possible number in num1 and num2, using monotonically decreasing stack
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        
        def getK(nums, k):
            n = len(nums)
            to_pop = n - k
            ans = []
            
            for num in nums:
                while len(ans) > 0 and num > ans[-1] and to_pop > 0:
                    to_pop -= 1
                    ans.pop()
                ans.append(num)
            return ans[:k]
            
        def getMax(nums1, nums2):
            ans = []
            while nums1 and nums2:
                if nums1 > nums2:
                    ans.append(nums1.pop(0))
                else:
                    ans.append(nums2.pop(0))
                    
            if nums1:
                ans.extend(nums1)
            else:
                ans.extend(nums2)
                
            return ans
        
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        
        for k1 in range(k + 1):
            k2 = k - k1
            if k1 > n1 or k2 > n2:
                continue
            ans = max(ans, getMax(getK(nums1,k1), getK(nums2, k2)))
            
        return ans
    
#单调递减栈 时间复杂度O(k**2(m+n))    
class Solution2(object):
    def maxNumber(self, nums1, nums2, k):

        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k #生成长度为k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        return max(merge(pick_max(nums1, i), pick_max(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))
    '''
          0 <= i <= n1   0 <= k - i <= n2
         i = max(0, k - n2)  i <= min(k, n1)

'''''
nums1 = [3, 4, 6, 5]        -> 6 5
nums2 = [9, 1, 2, 5, 8, 3]  -> 9 8 3
k = 5
输出:
[9, 8, 6, 5, 3]

