from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cumulative_left = []
        product = 1
        for index in range(len(nums)):
            product *= nums[index]
            cumulative_left.append(product)

        cumulative_product = 1
        for index in range(len(nums) - 1, -1, -1):
            if index == 0:
                cumulative_left[index] = cumulative_product
            else:
                product = cumulative_left[index - 1] * cumulative_product
                cumulative_left[index] = product
            cumulative_product = cumulative_product * nums[index]
        return cumulative_left

## nums = [1, 2, 4, 6]
## res = productExceptSelf(nums)
## print(res)

## nums2 = [-1, 0, 1, 2, 3]
## res2 = productExceptSelf(nums2)
## print(res2)

## nums2 = [0, 0]
## res2 = productExceptSelf(nums2)
## print(res2)

## nums = [0, 8, 0]
## res = productExceptSelf(nums)
## print(res)

nums = [1, 2, 3, 4]
res = Solution().productExceptSelf(nums)
print(res)
