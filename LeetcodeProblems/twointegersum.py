#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# Brute Force Method is going to be the best bet to solve
# n * n = o(n2)
# Hash Map Method - mapping each value of the index to the value of the array. One Pass (conceptual)
# Time : o(n)
# memory : o(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
