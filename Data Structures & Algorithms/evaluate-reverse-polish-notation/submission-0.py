class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        temp = []
        out = 0
       
        op = ['+', '-', '*', '/']
        while tokens: 
            token = tokens.pop(0)
            if token in op:
                num1 = temp.pop()
                num2 = temp.pop()
                if token == '+':
                    out = num2 + num1
                if token == '*':
                    out = num2 * num1
                if token == '-':
                    out = num2 - num1
                if token == '/':
                    out = num2 / num1
                temp.append(int(out))
            else:
                temp.append(int(token))
            
        
        return temp[0]