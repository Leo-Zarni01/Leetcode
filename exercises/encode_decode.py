from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        combined_str = ""
        for each_string in strs:
            combined_str += each_string
            combined_str += "\n"
        return combined_str

    def decode(self, s: str) -> List[str]:
        print("To analyze: ", s)
        strings = []
        current_charc = ""
        for each_character in s:
            if each_character == "\n":
                print("To add to list: ", current_charc)
                strings.append(current_charc)
                current_charc = ""
            else:
                current_charc += each_character
        return strings

example_1 = Solution()
example_1_encode = Solution().encode(["neet","code","love","you"])
example_1_decode = Solution().decode(example_1_encode)
print(example_1_decode)
