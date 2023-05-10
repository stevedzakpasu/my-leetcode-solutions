# This code is a solution to the Group Anagrams problem, where given a list of strings `strs`, 
# the function `groupAnagrams` groups the anagrams together and returns a list of lists, 
# where each inner list contains the anagrams.

# The function begins by initializing an empty dictionary `ans` using `collections.defaultdict(list)`.
# This dictionary will store the anagrams as values, 
# with the key being a tuple representation of the character count of each letter in the anagram.

# It then iterates through each string `s` in the input list `strs` using a for loop.
# For each string `s`, it initializes a list `count` of size 26, 
# representing the count of each letter in the string.

# Next, it iterates through each character `c` in `s` using another for loop 
# and increments the corresponding count in the `count` list.
#  This is done by calculating the index of 
# the character `c` in the `count` list using the expression `ord(c) - ord("a")` 
# (assuming all characters are lowercase English letters). The count is incremented by
# 1 for each occurrence of the character `c` in the string `s`.

# After iterating through all the characters in `s` and updating the `count` list accordingly,
# the code converts the `count` list into a tuple using `tuple(count)`. This tuple serves as the key in the dictionary `ans`.

# Finally, it appends the string `s` to the list of values corresponding to the key `tuple(count)` 
# in the `ans` dictionary using the `append` method.

# Once the for loop completes for all strings in `strs`, 
# the function returns the values of the `ans` dictionary using the `values` method, 
# which gives us a list of lists containing the grouped anagrams.

# Overall, this solution has a time complexity of O(n*m),
# where n is the number of strings in `strs` and m is the maximum length of a string in `strs`.
# This is because the code iterates through each string in `strs` and each character in each string,
# performing constant time operations (lookup, increment, and tuple creation) on the dictionary `ans`.



import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
