Given an integer array `nums`, return an array answer such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
## $\text{Specification}$.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in $O(n)$ time and without using the division operation.

## $\text{Algorithm}$.
1. Initialize an empty array `cumulative_left` that will later store the cumulative product of every number up to and not including the current number in the array
2. Go through the `nums` array from the left, populating the empty array `cumulative_left` with values
3. Go through the `nums` array from the right this time, replacing the values from `cumulative_left` accordingly:
  1. Initialize a variable $\text{cumulative product}$ which we will use to multiply with values from `nums`
  2. If $i \neq 0$,
    1. Let $\text{product(i)} = \text{left}(i - 1) * \text{cumulative product}$ where $i \neq 0$
    2. Replace $\text{cumulative left}(i)$ with $\text{product}(i)$ if $i \neq 0$
    3. Update $\text{cumulative product}$ by multiplying with $\text{nums}(i)$ (Refer to 3.1.)
  3. Otherwise,
    1. Let $\text{cumulative left}(i) = \text{cumulative product}$ 
4. Return the array $\text{cumulative left}$
