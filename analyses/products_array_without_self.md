## $\text{Specification}$.
Given an integer array `nums`, return an array answer such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in $O(n)$ time and without using the division operation.

## $\text{Algorithm}$.
1. Initialize an empty array `cumulative_left` that will later store the cumulative product of every number up to and not including the current number in the array
2. Go through the `nums` array from the left, populating the empty array `cumulative_left` with values
3. Go through the `nums` array from the right this time, replacing the values from `cumulative_left` accordingly:
  1. Initialize a variable `cumulative product` which we will use to multiply with values from `nums`
  2. If `i ≠ 0` then replace `cumulative_left[i]` with `product[i]`
  3. Let `product[i] = left[i - 1]` $\times$ `cumulative_product`
  4. Update `cumulative_product` by multiplying with `nums[i]` (Refer to 3.1.)

4. If `i != 0`:
   1. Let `cumulative_left[i] = cumulative_product`
5. Return the array `cumulative_left`
