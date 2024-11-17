# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#
# Please implement encode and decode
# Example 1:
    # Input: ["lint","code","love","you"]
    # Output: ["lint","code","love","you"]
    # Explanation:
    # One possible way of encoding is: "lint code love you"

import re


class Soultion:
    """
    @param strs: a list of strings
    @return: encodes a list of strings to a single string
    """

    def encode(self, strs):
       res = ""
       for s in strs:
           res += str(len(s)) + "#" + s
       return res

    def decode(self, str):
        """
        @param str: a string
        @return: decodes a single string to a list of strings
        """

        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

# Time complexity: O(m) for encode() and decode()
# Space complexity: O(n) for encode() and decode()
# m is the sum of lengths of all strings and n is the number of strings
