from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index in range(len(numbers)):
            slow_index = index
            fast_index = slow_index + 1
            current = numbers[slow_index]
            difference = target - current
            print(f"Current number is: {current}")
            print("Difference is: ", difference)
            
            for inner_index in range(fast_index, len(numbers)):
                fast = numbers[inner_index]
                print("Testing with ", fast)
                if fast == difference:
                    return [slow_index + 1, inner_index + 1]
            print()
        return []

demo_one = Solution()
nums_one = [2,3,4]
target = 6
test_one = demo_one.twoSum(nums_one, target)
print(test_one)
