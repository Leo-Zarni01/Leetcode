class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## first convert input string to valid alphanumeric only string

        s_list = s.split()

        new_string = ""
        for each in s_list:
            word = ""
            for a in each: ## canal: => canal
                if a.isalnum():
                    word += a
            new_string += word

        new_string = new_string.lower()
        front = 0
        end = len(new_string) - 1

        if len(s_list) == 0:
            return True

        lowercase = new_string.lower()
        while front < end:
            if lowercase[front] != lowercase[end]:
                return False ## the moment we detect an inversion, i.e., if there is any invalid matching, break the loop and return False
            front += 1
            end -=1
        return True ## by default we assume the given word is a palindrome