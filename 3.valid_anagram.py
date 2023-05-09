

# This code is a solution to the Anagram problem, where given two strings s and t, 
# the function isAnagram returns True if s and t are anagrams (i.e., contain the same letters with the same frequency)
# and False otherwise.

# The function first checks if the lengths of s and t are equal.
# If not, it returns False because two strings with different lengths cannot be anagrams.

# If the lengths are equal, the function initializes two empty dictionaries countS and 
# countT to keep track of the frequencies of letters in s and t, respectively.

# It then iterates through the characters of s and t using a for loop and for each character,
# it updates the countS and countT dictionaries.
# The expression countS[s[i]] = 1 + countS.get(s[i], 0) increments the count of the character s[i] in countS by 1, 
# or initializes it to 1 if it does not already exist in the dictionary. The same is done for t[i] in countT.

# Finally, the function returns True if countS and countT are equal (i.e., contain the same keys with the same values)
# and False otherwise.

# Overall, this solution has a time complexity of O(n) 
# because it iterates through the characters of s and t once, 
# and performs constant time operations (lookup and insertion) on the dictionaries countS and countT.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
