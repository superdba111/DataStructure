# -*- coding: utf-8 -*-
"""
Created on Sun May 13 12:16:18 2018

@author: yli

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

# Definition for singly-linked list.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strList = [str(i) for i in digits]

        newNumber = int(''.join(strList))+1

        newList = [int(i) for i in list(str(newNumber))]
        return newList  
    
if __name__ == "__main__":
    
    
    l1 = [1,2,3]
    l2 = [4,3,2,1]

    
    test = Solution()

    print(test.plusOne(l1))
    print(test.plusOne(l2))