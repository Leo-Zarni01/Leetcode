from typing import List

## O (n log n solution)
# class Solution:
#     def binarySearch(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) -1 
#         while left <= right:
#             middle = (left + right) // 2
#             if nums[middle] < target:
#                 left = middle + 1
#             elif nums[middle] > target:
#                 right = middle - 1
#             else:
#                 return middle
#         return -1

#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for each_row in matrix:
#             search_status = self.binarySearch(each_row, target)
#             if search_status == -1:
#                 continue
#             else:
#                 return True
#         return False

## O log mn solution
class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1 
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) -1 
        while top <= bottom:
            row = (top + bottom) // 2
            leftmost = matrix[top][-1]
            rightmost = matrix[bottom][0]
            if leftmost < target:
                top = row + 1
            elif rightmost > target:
                bottom = row - 1
            else:
                break
        
        if top > bottom:
            return False
        
        search_status = self.binarySearch(matrix[row], target)
        if search_status == -1:
            return False
        return True

