def convert_string_to_list(input_string):
    return list(input_string)

def check_pairs(closed, opened):
    if closed == ")" and opened == "(":
        return True
    elif closed == "}" and opened == "{":
        return True
    elif closed == "]" and opened == "[":
        return True
    return False

def is_closed(bracket):
    if bracket in [")", "}", "]"]:
        return True
    return False

def isValid(s):
    ## edge cases
    if (len(s) == 1): ## valid bracket strings are of length >= 2
        return False
    else:
        if not is_closed(s[-1]): ## ()[ => false
            return False

    ## creating stack
    stack = []
    s_list = convert_string_to_list(s)
    for each_bracket in s_list:
        stack.append(each_bracket)
    print("Initial stack: ", stack)

    ## algo
    end = False
    while end is False:
        current = stack.pop()
        next = stack.pop()
        print(f"Current: {current}, next: {next}")

        match = check_pairs(current, next)
        print("Are they matching pairs?", match)
        if len(stack) == 0:
            if match is True:
                return True
            else:
                return False
        else:
            if not match:
                print(f"Is {next} closed?", is_closed(next))
                if not is_closed(next):
                    return False
                else:
                    copy_stack = [next]
            else:
                copy_stack = []
            print("Remaining stack: ", stack)
            while len(stack) != 0:
                dummy_pop = stack.pop()
                print("Inside: ", dummy_pop)
                print(f"Comparing: {current} and dummy: {dummy_pop}", check_pairs(current, dummy_pop))
                if (check_pairs(current, dummy_pop) and len(copy_stack) == 0):
                    break
                else:
                    copy_stack.append(dummy_pop)
                print()
            print("Copy: ", copy_stack)
            for each_bracket in reversed(copy_stack):
                stack.append(each_bracket)
            print("new stack:", stack)
        print()
        print()

# example_one = "[]"
# print(isValid(example_one))

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