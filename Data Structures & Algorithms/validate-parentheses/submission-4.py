class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        mapping = {'(': ')', '{': '}', '[': ']'}
        temp_stack = []  # Stack to store opening brackets

        for char in s:
            if char in mapping:  # If it's an opening bracket
                temp_stack.append(char)
            else:  # It's a closing bracket
                if not temp_stack:
                    return False
                elif mapping[temp_stack.pop()] != char:
                    return False

        # Stack should be empty if all brackets are matched
        return not temp_stack
            