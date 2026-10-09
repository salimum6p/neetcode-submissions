class Solution:
    
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
          try:
            value = int(token)
            stack.append(value)
          except ValueError:
            match token:
              case '+':
                value1, value2 = stack.pop(),stack.pop()
                stack.append((value1 + value2))
              case '-':
                value1, value2 = stack.pop(),stack.pop()
                stack.append((value2 - value1))
              case '*':
                value1, value2 = stack.pop(),stack.pop()
                stack.append((value1 * value2))
              case '/':
                value1, value2 = stack.pop(),stack.pop()
                stack.append(int(value2 / value1))
        return stack[-1]
    


