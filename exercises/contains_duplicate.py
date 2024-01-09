from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        curr_index = 0
        neighbor = 1
        # counts = {}
        while curr_index < len(nums) - 1:
            if nums[curr_index] == nums[neighbor]:
                return True
            curr_index += 1
            neighbor += 1
        return False