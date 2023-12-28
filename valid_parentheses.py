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
    if not is_closed(s[-1]): ## ()[) => false
        return False

    ## creating stack
    stack = []
    s_list = convert_string_to_list(s)
    for each_bracket in s_list:
        stack.append(each_bracket)

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
            copy_stack = []
            if not match:
                while len(stack) != 0:
                    copy_stack.append(stack.pop())
            print("Copy: ", copy_stack) 

# example_one = "[]"
# print(isValid(example_one))

example_two = "[]()"
print(isValid(example_two))