from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0
        for _ in range(len(height)):
            left_bound = height[left_pointer]
            right_bound = height[right_pointer]
            print(f"Left is {left_bound} and right is: {right_bound}")

            min_y = None
            delta_x = abs(left_pointer - right_pointer)

            if left_bound <= right_bound:
                min_y = left_bound
                left_pointer += 1
            else:
                min_y = right_bound
                right_pointer -= 1
            print(f"Area is {delta_x} * {min_y}")
            area = delta_x * min_y
            if area > max_area:
                max_area = area
            print()
        return max_area

demo_one = Solution()
height = [1,8,6,2,5,4,8,3,7]
test_one = demo_one.maxArea(height)
print(test_one)
print()
