class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closed_to_open = {
            ')': '(',
            '}':'{',
            ']':'['
        }

        for char in s:
            if char not in closed_to_open:
                stack.append(char)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if popped != closed_to_open[char]:
                    return False
        return len(stack) == 0   
        