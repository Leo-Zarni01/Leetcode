"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""

def get_number_to_mod(number_string):
    # returns the number to mod in int format
    length_string = len(number_string)
    number_to_mod = int("1" + ("0" * (length_string - 1)))
    return number_to_mod

def romanToInt(number_string):
    symbols = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    special_cases = {4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}
    target_number = number_string
    cur_string = ""
    while target_number != "0":
        number_to_mod = get_number_to_mod(target_number)
        floor_div = int(target_number)//number_to_mod
        current_num_to_rom = floor_div * number_to_mod
        remainder = int(target_number) % number_to_mod
        # print("current number is {}, and modding it with {}, remainder is: {}".format(target_number, number_to_mod, remainder))
        # print("current number to convert:", current_num_to_rom)

        if current_num_to_rom in special_cases:
            cur_string += special_cases[current_num_to_rom]
        else:
            cur_string += symbols[number_to_mod] * floor_div
        #print(cur_string)
        target_number = str(remainder)
        #print()
        
# print(romanToInt("333"))
# romanToInt("321")
# romanToInt("3")
# romanToInt("4")
# romanToInt("9")
# romanToInt("39")
romanToInt("3999")



