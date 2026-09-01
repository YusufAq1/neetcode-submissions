class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) <= 1:
            return False

        open = ['(', '{', '[']

        open_close = {')' : '(',
                        '}' : '{',
                        ']': '['}

        close = [')', '}', ']'] 

        open_stack = []

        for bracket in s:
            if bracket in open:
                open_stack.append(bracket)
            else:
                if len(open_stack) > 0:
                    open_bracket = open_stack[-1]
                    if open_bracket == open_close.get(bracket):
                        open_stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(open_stack) > 0:
            return False
        else:
            return True


