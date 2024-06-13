#Given an array of string strs, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
    # Input: strs = ["act","pots","tops","cat","stop","hat"]
    #Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Time Complexity = O(m * nlogn)
# count [a-z] = 1e, 1a, 1t

# Hash Map Method
# Key: [eat,tea]
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) #mapping the charCount to list of Anagrams
        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1

            anagrams[tuple(count)].append(s)
        return anagrams.values()
