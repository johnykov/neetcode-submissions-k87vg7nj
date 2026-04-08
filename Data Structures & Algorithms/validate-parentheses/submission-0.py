class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        mapping = {")": "(", "}": "{", "]": "["}
        
        for c in s:
            if c in mapping:
                topel = stack.pop() if stack else '#'
                if topel != mapping[c]:
                    return False
            else:
                stack.append(c)
        return not stack
        