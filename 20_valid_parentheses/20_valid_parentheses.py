# 20. Valid Parentheses
# Solved
# Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closing_brackets = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        for ch in s:
            if ch in closing_brackets:
                if stack and stack[-1] == closing_brackets[ch]:
                    stack.pop()  # repeatadle remove last element until nothing left in stack
                else:
                    return False
            else:
                stack.append(ch)

        return not stack  # should finish with an empty stack