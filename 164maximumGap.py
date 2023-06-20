# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:13:42 2019

@author: liuga
"""

#桶排序，空间复杂度O(n) 后一个桶的最小值与前一个桶的最大值之差作为两个桶的间距， 相邻数字的间距都小于⌈(max−min)/(N−1)⌉
#桶左闭右开 [1,3)
class Solution2(object):
    def maxinumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0

        #初始化
        max_ = max(nums)
        min_ = min(nums)
        max_gap = 0

        each_bucket_len = max(1, (max_ - min_)// (n -1)) #地板除法和int()取整类似，去掉小数部分向下取整，只取整数部分
        buckets = [[] for _ in range((max_ - min_)//each_bucket_len +1)] #+1最后一个桶放最大的数. 更为严谨，相对下面n+1(特殊设定)

        #把数字放进桶里
        for i in range(len(nums)):
            index = (nums[i] - min_)//each_bucket_len
            bucket[index].append(nums[i])

        #遍历桶更新答案
        prev_max = float('inf')
        for i in range(len(buckets)):
            if bucket[i] and prev_max != float('inf'):
                max_gap = max(max_gap, min(bucket[i]) - prev_max)

            if buckets[i]:
                prev_max = max(buckets[i])

        return max_gap
            
        #改写
        prev_max = max(buckets[0])
        for i in range(1, n+1):
            if not buckets[i]:
                continue
            bucket_min = min(buckets[i])
            max_gap = max(max_gap, bucket_min - prev_max)
            prev_max = max(buckets[i])
        return max_gap
            
        
    
#suppose there are N elements and they range from min_val to max_val. 桶排序要牺牲O(n)的空间复杂度
#设置N+1个桶是保证一定有个空桶，最大间距必然不来自一个桶
#Then the maximum gap will be no smaller than size = ceiling[(max_val -min_val)/(N - 1)],一共n+1个桶，最后一个桶存最大值，n个数放在n+1个桶，必然存在空桶，最大间距必然不来自同一个桶

#把每个数都放进各自的桶里，nums[i]应该放在第(nums[i]-min_val)//size个桶里，每个桶只存储该桶内的最小值和最大值，格式为[min,max], 排除掉空桶后，求相邻两个桶内数字的最大距离，即第i个桶的最小值和第i-1个桶的最大值之间的差
class Solution2(object):
    def maximumGap2(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        min_val = min(nums)
        max_val = max(nums)

        if max_val == min_val:
            return 0
        #桶长度 向上取整数 防止取0， 另一种方式桶尺寸更小一点 size == (max_val - min_val)//(n-1) or 1
        size = math.ceil((max_val - min_val)/(n-1))

        bucketSize = ((max_val - min_val) // size) + 1

        #最小值 最大值 数组 range((max_val - min_val)//size +1) 加1保证了数组的最大值也能分到一个桶 
        buckets = [[float('inf'), float('-inf')] for _ in range(bucketSize)] 
        
        for num in nums:
            b = buckets[(num - min_val)//size]
            b[0] = min(b[0], num) 
            b[1] = max(b[1], num) 

        buckets = [b for b in buckets if b[0] != float('inf')] #去除空桶
        return max(buckets[i][0] - buckets[i-1][1] for i in range(1, len(buckets)))
