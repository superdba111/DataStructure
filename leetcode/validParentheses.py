# -*- coding: utf-8 -*-
"""
Created on Sun May 13 22:04:43 2018

@author: yli

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack=[]
        for x in s:
            if len(stack)==0:
                stack.append(x)
            elif x=='('or x=='['or x=='{':
                stack.append(x)
            else:
                if (stack[-1]=="{" and x=="}")or(stack[-1]=="[" and x=="]")or(stack[-1]=="(" and x==")"):
                    stack.pop(-1)
                    continue
                else:
                    return False
        return True if len(stack)==0 else False
    
    
if __name__ == "__main__":
    
    
    s1 = "{[]}"
    s2 = "([)]"

    
    test = Solution()

    print(test.isValid(s1))
    print(test.isValid(s2))    