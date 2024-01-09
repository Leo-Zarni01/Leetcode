def return_special_cases(character, target):
    if character == "I":
        if (target == "V"):
            return (4, True)
        elif (target == "X"):
            return (9, True)
        else:
            return (returnRomanValues(character), False)
    elif character == "X":
        if target == "L":
            return 40,True
        elif target == "C":
            return 90, True
        else:
            return (returnRomanValues(character), False)
    elif character == "C":
        if target == "D":
            return 400, True
        elif target == "M":
            return 900, True
        else:
            return (returnRomanValues(character), False)
    else:
        return (returnRomanValues(character), False)

def convert_string_to_list(number_string):
    return list(number_string)

def returnRomanValues(character):
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10, 
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    return symbols[character]

def romanToInt(number_string):
    number_list = convert_string_to_list(number_string)
    i = 0
    value = 0
    while i <= len(number_list) - 1:
        current = number_list[i]
        # print("Current value: ", value)
        if i + 1 <= len(number_list) - 1:
            ## compare with neighbor
            neighbor = number_list[i+1]
            # print(f"Current comparison: {current}, {neighbor}")
            res_tuple = return_special_cases(current, neighbor)
            # print(res_tuple)
            value += res_tuple[0]
            if res_tuple[1] == True:
                i += 2
            else:
                i += 1
        else:
            value += returnRomanValues(current)
            i += 1
    return value

# example_one = "III"
# print(romanToInt(example_one))
# print()

# example_two = "LVIII"
# print(romanToInt(example_two))

# example_three = "MCMXCIV"
# print(romanToInt(example_three))

# example_four = "DCXXI"
# print(romanToInt(example_four)) 

example_five = "MCDLXXVI"
print(romanToInt(example_five)) ## expected 1476, received 1576 (fixed)