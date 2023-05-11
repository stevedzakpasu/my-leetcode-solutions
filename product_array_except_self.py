# This code is a solution to the Product of Array Except Self problem.
# Given an array of integers `nums`, the function `productExceptSelf`
# returns a new array where each element at index `i` contains the product 
# of all the elements in the original array except the element at index `i`.

# The function begins by creating a new list `res` of the same length as `nums`
# and initializing all its elements to 1 using the expression `[1] * (len(nums))`.
# This list will store the resulting products.

# The code then initializes two variables `prefix` and `postfix` to 1. 
# These variables will keep track of the product of elements before 
# and after the current index, respectively.

# The first loop iterates through the indices of `nums` using a range-based for loop. 
# For each index `i`, it assigns the value of `prefix` to the corresponding index `i` 
# in the `res` list, effectively storing the product of all the elements before the current index.

# After assigning the value of `prefix` to `res[i]`, it updates the value of `prefix` by multiplying
# it with the value at `nums[i]`. This way, `prefix` keeps track of the product of elements encountered so far.

# The second loop iterates through the indices of `nums` in reverse order using
# a range-based for loop. Starting from the last index, it assigns the product of `res[i]`
#  and `postfix` to `res[i]`. This step multiplies the product of elements before 
# `i` (stored in `res[i]`) with the product of elements after `i` (stored in `postfix`), 
# effectively computing the product of all elements except the one at the current index.

# Similar to the first loop, it updates the value of `postfix` by multiplying it with the
# value at `nums[i]`, which allows it to keep track of the product of elements encountered in reverse order.

# Finally, the function returns the resulting list `res`, which contains the product of
# all elements except self at each index.

# The overall time complexity of this solution is O(n) since it iterates through the `nums
# array twice, once in each loop, where `n` is the length of `nums`.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
