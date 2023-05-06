# This code is a solution to the Two Sum problem,
# where given an array of integers nums and a target integer target,
# the function twoSum returns a list of two indices that correspond 
# to the positions of two numbers in the input array whose sum is equal to the target.
# The function uses a dictionary prevMap to store the previously visited numbers
# as keys and their indices as values.
# It then iterates through the input array using a for loop and for each number n,
# it calculates the difference diff between the target and the current number.
# If the difference diff is already in the prevMap dictionary,
# it means that we have found the required pair of numbers whose sum equals the target.
# In that case, the function returns a list of two indices:
# the index of the previously visited number (stored as value in prevMap)
# and the index of the current number (i). Otherwise,
# the function adds the current number n to the prevMap dictionary with its index i.
# Overall, this solution has a time complexity of O(n)
# because it visits each number in the array at most once
# and performs constant time operations (lookup and insertion) on the dictionary.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store previously visited numbers and their indices
        prevMap = {}  # val -> index

        # Iterate through the input array using a for loop
        for i, n in enumerate(nums):
            # Calculate the difference between the target and the current number
            diff = target - n
            
            # Check if the difference exists in the prevMap dictionary
            if diff in prevMap:
                # If it does, return a list of two indices: the index of the previously visited number and the current number
                return [prevMap[diff], i]
            
            # If the difference does not exist in the prevMap dictionary, add the current number and its index to the prevMap dictionary
            prevMap[n] = i
        
        # If no solution is found, return an empty list
        return []
    


