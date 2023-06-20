# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:57:53 2019

@author: liuga
"""
#扩展，如果有负数？ python负数除法和java c++不一样  abs(nums[i] - nums[j]) <= t ，同时 abs(i - j) <= k
#nums = [1,2,3,1], k = 3, t = 0
import collections
class Solution(object):
    def containdulicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        
        dict = collections.OrderedDict()
        
        for i in range(len(nums)):
            key = nums[i]/max(k, 1)
            for m in (key - 1, key, key + 1):
                if m in dict and abs(nums[i] - dict[m]) <= t:
                    return True
            dict[key] = nums[i]
            if i >= k:
                dict.popitem(last = False) #remove the first entry from dict
        return False
                    

#红黑树解法
class Solution(object):
    def containNearbyDuplicate(self, nums, k, t):
        from sortedcontainers import SortedList
        window = SortedList()
        n = len(nums)
        left = 0
        right = 0

        if k == 0 ir n in (0,1)
        return False

        while right < n:
            window.add(nums[right])
            if right == 0: #如果是第一个 跳过
                right += 1
                continue

            idx = window.bisect_left(nums[right]) #窗口内的排序
            if idx > 0 and abs(window[idx]- window[idx -1] <= t):
                return True

            if idx < len(window) -1 and abs(window[idx+1] - window[idx]) <= t:
                return True

            if right > = k:
                windows.remove(nums[left])
                left += 1
                
            right +=1

        return False
    
            

import bisect
import sortedContainers
class Solution3(object):
    def containsNearbyDuplicate(self, nums, k, t):
        k += 1
        temp = sortedContainers.SortedList(nums[:k])
        for i in range(1, len(temp)):
            if temp[i] - temp[i-1] <= t:
                return True

        for i in range(1, len(nums)-k+1):
            num = nums[i+k-1]
            temp.remove(nums[i-1])
            temp.add(nums[i+k-1])

            idx = bisect.bisect_left(temp, num)

            if (idx-1 >=0 and num-temp[idx-1] <= t) or (idx+1 < k and temp[idx+1] - num <= t):
                return True

            return False
            
                
                     
#bucket sort. each bucket has the size of t+1. for each number, the possible candicate should be in the same bucket or 2 buckets besides.
#keep as many as k buckets to ensure the difference is at most k.
        def containsNearbyDuplicate(self, nums, k, t):
            if t == 0 and len(nums) == len(set(nums)): #t = 0 is special case, which require at least one pair of repeated element
                return False
            buckets = {}
            width = t + 1
            for i , v in enumerate(nums):
                bucketNum = v//width  # bucketNum = getIdx(v)
                offset = 1
                for idx in xrange(bucketNum - offset, bucketNum + offset +1):
                    if idx in buckets and abs(buckets[idx] - nums[i]) < width: #<= t
                        return True
                buckets[bucketNum] = nums[i]
                if i >= k: #维护个数为k， 删除下标范围不在[max(0, i-k), i）内的桶，比如遍历到2，删除0对应的桶
                    del buckets[nums[i-k]//width]

            return False
        
        def getIdx(u):
            return ((u + 1) // size) - 1 if u < 0 else u // size  #分成[-4,-3,-2,-1], [0,1,2,3]

#此题为准 
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if not nums or indexDiff <= 0 or valueDiff < 0:
            return False

        mini = min(nums)
        diff = valueDiff + 1
        bucket = {}

        def getKey(num: int) -> int:
            return (num - mini) // diff

        for i, num in enumerate(nums):
            key = getKey(num)
            if key in bucket:  # Current bucket
                return True
            # Left adjacent bucket
            if key - 1 in bucket and num - bucket[key - 1] < diff:
                return True
            # Right adjacent bucket
            if key + 1 in bucket and bucket[key + 1] - num < diff:
                return True
            bucket[key] = num
            if i >= indexDiff:
                del bucket[getKey(nums[i - indexDiff])]

        return False

#建立目标桶，并删除下标范围不在 [max(0,i−k),i) 内的桶(i只需要看前面的桶是否有效[i-k,i]) 有效的桶是下标为[i-k,i+k]的元素构造的桶, 如果nums[i-(k+1)]产生的桶存在，我们要把其删除掉。因为abs(i-(i-(k+1))) = abs(k+1) = k+1 > k
#任何时候我们每个桶中最多只可能有一个元素? 有2个元素可以直接返回True
class Solution(object):
    def containsNearbyDuplicate(self, nums, k, t):
        bucket = defaultdict(list)
        for idx, num in enumerate(nums):
            bid = num//(t+1)
            #提前删除窗口外的桶，以免影响判断
            if idx -(k+1) >=0  :
                dropid = nums[idx - k - 1]// (t+1)
                del bucket[dropid]
            #当前桶里面有没有元素
            if len(bucket[bid]) > 0:
                return True
            #前面的桶有元素和num的绝对值差小于 t
            if bucket[bid-1] and abs(bucket[bid-1][0] - num) <= t:
                return True
            #后面的桶元素和num的绝对值差小于 t
            if bucket[bid+1] and abs(bucket[bid+1][0] - num) <= t:
                return True
            bucket[bid].append(num) #把这个元素放入其属于的桶
        return False
