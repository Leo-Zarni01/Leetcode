from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        for _ in range(len(numbers)):
            left_num = numbers[left]
            right_num = numbers[right]
            if left_num + right_num > target:
                right -= 1
            elif left_num + right_num < target:
                left += 1
            elif left_num + right_num == target:
                return [left + 1, right + 1] # because array is 1-indexed
        return []

demo_one = Solution()
nums_one = [2,3,4]
target = 6
test_one = demo_one.twoSum(nums_one, target)
print(test_one)
