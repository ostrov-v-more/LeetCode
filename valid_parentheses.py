"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
strs1 = "([)]"  # false
strs2 = ')(({}[{(}])))'  # false
strs3 = '(]}'  # false
strs4 = "()[]{}"  # true
strs5 = ')('

class Solution:
    def isValid(self, s: str):  # -> bool:
        lst = []
        for v in s:
            if v in '([{':
                lst.append(v)
            elif len(lst) != 0:
                if v in ')' and lst[-1] == '(':
                    lst.pop()
                elif v in ']' and lst[-1] == '[':
                    lst.pop()
                elif v in '}' and lst[-1] == '{':
                    lst.pop()
                else:
                    return False
            elif v in ')]}':
                return False
        return len(lst) == 0


    def isValid_2(self, s: str) -> bool:
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}

        for b in s:
            # open brackets case
            print(f'1: {b in brackets}')
            print(f'2: {not stack}')
            if b in brackets:
                stack.append(b)
                print(f'3: {stack}')
            # closed brackets case
            elif not stack or brackets[stack.pop()] != b:
                return False

        return len(stack) == 0

s = Solution().isValid_2(strs4)
print(s)

