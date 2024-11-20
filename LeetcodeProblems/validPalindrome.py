# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

#Example 1:
#Input: s = "Was it a car or a cat I saw?"
#Output: true

class Soultion:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1] # [::-1] reverses a string by starting from the end (-1) and moving backwards through the string

# Second solution (Two Pointers)
class Soultion:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1 # increment l
            while r < l and not self.alphaNum(s[r]):
                r -= 1 # decrement r
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + r, r - 1 # increment l and decrement r through the string
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
