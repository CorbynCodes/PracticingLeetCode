# Given the array of integer nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# For Brute Force method
# Time compleaxity: O(n2)
# Space complexity: 0(1)

# For Hash Set method
# Time complexity: O(n)
# Space complexity: O(n)

# using hashset method which is the most effecient way to solve this problem
class Soultion:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
