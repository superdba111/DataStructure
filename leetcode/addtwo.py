# -*- coding: utf-8 -*-
"""
Created on Fri May  4 11:36:27 2018

@author: yli

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []

        d = dict()

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            elif target ==( nums[i] + d[nums[i]]):
                return [d[nums[i]],i]

            n = target - nums[i]
            if n in d and i is not d[n]:
                return [d[n],i]

        return []
    
if __name__ == "__main__":
    
    n = [2, 7, 11, 15]
    t= 9

    test = Solution()

    print(test.twoSum(n,t))