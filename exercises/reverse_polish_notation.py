from typing import List
import math
class Solution:
    def operation(self, token: str, first_operand: int, second_operand: int) -> int:
        if token == "+":
            print(f"{first_operand} + {second_operand}")
            return first_operand + second_operand
        elif token == "-":
            print(f"{first_operand} - {second_operand}")
            return first_operand - second_operand
        elif token == "*":
            print(f"{first_operand} * {second_operand}")
            return first_operand * second_operand
        elif token == "/":
            print(f"{first_operand} // {second_operand}")
            return math.trunc(first_operand / second_operand)
        return 0

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for index in range(len(tokens)):
            print("Stack: ", stack)
            current = tokens[index]
            if current not in operators:
                stack.append(current)
            else:
                if len(stack) >= 1:
                    first = stack.pop()
                    second = stack.pop()
                    print(f"The first value is: {first} and the second value is: {second}")
                    evaluated_value = self.operation(current, int(second), int(first))
                    print("The evaluated value is: ", evaluated_value)
                    stack.append(evaluated_value)
            print()
        ## print("End of iteration, stack is: ", stack)
        return stack.pop()

# tokens = ["1","2","+","3","*","4","-"]
# demo_one = Solution()
# demo_one_res = demo_one.evalRPN(tokens)

# tokens = ["1","2", "3", "+", "-"]
# demo_one = Solution()
# demo_one_res = demo_one.evalRPN(tokens)

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
demo_one = Solution()
demo_one_res = demo_one.evalRPN(tokens)