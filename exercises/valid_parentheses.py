class Solution:
    def is_closed(self, bracket):
        if bracket in [")", "}", "]"]:
            return True
        return False
    
    def return_closed(self, bracket):
        if bracket == "{":
            return "}"
        elif bracket == "[":
            return "]"
        elif bracket == "(":
            return ")"
        return ""
    
    def isValid(self, s):
        stack = []
        for current_bracket in s:
            is_it_closed = self.is_closed(current_bracket)
            if not is_it_closed:
                close_bracket = self.return_closed(current_bracket)
                stack.append(close_bracket)
            else:
                if stack.pop() != current_bracket or len(stack) == 0:
                    return False
        if len(stack) >= 1:
            return False
        return True

example_one = "[]"

# example_two = "[]()"
# print(isValid(example_two))

# edge case condition 1
# example_three = "("
# print(isValid(example_three))

# edge case condition 2 
# example_four = "()("
# print(isValid(example_four))

# example_five = "(]"
# print(isValid(example_five))

# example_six = f"({{}})" 
# print(example_six)
# print(isValid(example_six))
        
# example_seven = "(]())()"
# print(isValid(example_seven))
        
# example_eight = "([)]"
# print(isValid(example_eight))
        
# example_nine = f"{{[]}}"
# print(example_nine)
# print(isValid(example_nine))
        
## example_ten = f"({{{{{{}}}}}})"
## print(example_ten)
## print(isValid(example_ten))
