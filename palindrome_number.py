"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Follow up: Could you solve it without converting the integer to a string?

"""
def isPalindrome(number):
    count = 0
    dummy = number 
    if dummy < 0:
        return False 
    remainder_lst = []
    while dummy != 0:
        remainder = dummy % 10
        remainder_lst.append(remainder)
        #print("remainder:", remainder, "when dummy is:", dummy)
        dummy //= 10
        #print("dummy number reduced to:", dummy)
        count += 1
        #print("count:", count)
        #print()
    #print("number of digits:", count)
    total = 0
    while count != 0:
        exp = 10**(count - 1)
        num = remainder_lst[len(remainder_lst)-count]*exp
        total += num
        count -= 1

    return total == number

    # count = 3 -> 1, 10, 100
    # count = 4 -> 1, 10, 100, 1000
print(isPalindrome(121))








