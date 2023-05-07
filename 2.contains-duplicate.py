# This code is a solution to the Contains Duplicate problem, where given an array of integers nums,
# the function containsDuplicate returns a boolean indicating 
# whether the input array contains any duplicates.
# The function uses a hashset to store the previously visited numbers.
# It then iterates through the input array using a for loop and for each number n,
# it checks if n is already in the hashset. If it is,
# it means that we have found a duplicate number in the input array.
# In that case, the function returns True.
# Otherwise, the function adds the current number n to the hashset.
# Overall, this solution has a time complexity of O(n) because it visits each number in the array at most once 
# and performs constant time operations (lookup and insertion) on the hashset


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
