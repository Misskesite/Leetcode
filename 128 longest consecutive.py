# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:53:11 2019

@author: liuga
"""
#查询为1 时间复杂度O(n)
class Solution(object):
    def longestConsercutive(self, nums):
        longest = 0
        num_set = set(nums)
        
        for num in num_set:
            
            if num - 1 not in num_set:
                cur_num = num
                cur_len = 1
            
                while cnum + 1 in num_set:
                    cur_num += 1
                    cur_len += 1
                    
                longest = max(longest, cur_len)
                
         return longest
        

class Solution2(object):
    def longestConsecutive(self, nums):
        hash_dict = dict() #保存当前字符对应的最长连续字符？

        max_len = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0) #获取键对应的值
                right = hash_dict.get(num + 1, 0)

                cur_len = 1 + left + right
                
                res = max(res, cur_len)

                hash_dict[num] = cur_len
                hash_dict[num - left] = cur_len
                hash_dict[num - right] = cur_len

        return max_len


#时间复杂度O(n), 空间复杂度O(n)
class Solution3(object):
    def longestConsecutive(self, num):
        mp  = {}
        for i in num:
            mp[i] = True

        res = 0
        for k, v in mp.items():
            if not v:  #已经搜过,跳出
                continue
            l = k - 1
            r = k + 1

            while mp.has_key(l) and mp[l]:
                mp[l] = False  #搜索过的元素的Value置为False, 避免重复搜索
                l -= 1

            while mp.has_key(r) and mp[r]:
                mp[r] = False
                r += 1

            n = r - l - 1
            res = max(res, n)

        return res
            

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
      ans = 0
      seen = set(nums)

      for num in nums:
          if num - 1 in seen: #If the number before current number  in set, then this path has already be traversed           
              continue
          length = 0
          while num in seen:
              num += 1
              length += 1
          ans = max(ans, length)

      return ans
