from typing import List
import math

def multiply(nums: List[int]) -> int: 
    result = math.prod(nums)
    return result

def productExceptSelf(nums: List[int]) -> List[int]:
    res = nums.copy()
    for index in range(len(nums)):
        print("Current number is: ", nums[index])
        left = nums[:index].copy()
        right = nums[index + 1:].copy()
        print("Left is: ", left)
        print("right is: ", right)
        left_product = multiply(left)
        right_product = multiply(right)
        total = left_product * right_product
        print("New number is: ", total)
        res[index] = total
        print()
    return res

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
res = productExceptSelf(nums)
print(res)
