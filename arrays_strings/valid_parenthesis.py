"""Valid Parenthesis.

Task: Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in mapping:
                if not stack:
                    return False
                elif stack.pop() == mapping[char]:
                    continue
                else:
                    return False
            else:
                stack.append(char)

        return not stack
