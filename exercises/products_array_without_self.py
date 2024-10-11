from typing import List
import math

def multiply(nums: List[int]) -> int: 
    result = 0
    if len(nums) >= 1:
        result = math.prod(nums)
    return result

def productExceptSelf(nums: List[int]) -> List[int]:
    res = nums.copy()
    for index in range(len(nums)):
        temp = []
        for other_index in range(len(nums)):
            if index == other_index:
                continue
            temp.append(nums[other_index])
        print("To multiply: ", temp)
        product = multiply(temp)
        print("Product is: ", product)
        res[index] = product
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

nums = [0, 8, 0]
res = productExceptSelf(nums)
print(res)
