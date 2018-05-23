# -*- coding: utf-8 -*-
"""
Created on Tue May 22 21:19:34 2018

@author: yli

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[int(len(nums)/2)]
    
if __name__ == "__main__":
    
    l1 = [3,2,3]
    
    l2 = [2,2,1,1,1,2,2]

    test = Solution()

    print(test.majorityElement(l1))
    
    print(test.majorityElement(l2))