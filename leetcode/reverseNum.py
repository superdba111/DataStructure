# -*- coding: utf-8 -*-
"""
Created on Fri May  4 11:55:14 2018

@author: yli


Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >=0:
            n = int(str(x)[::-1])
            if n >= 2**31-1:
                return 0
            else:
                return n
        else:
            t = int("-" + str(x)[::-1][:-1])
            if t <= -2**31:
                return 0
            else: 
                return t

    
if __name__ == "__main__":
    
    n = int(input("your number?  "))
    
    test = Solution()

    print(test.reverse(n))

