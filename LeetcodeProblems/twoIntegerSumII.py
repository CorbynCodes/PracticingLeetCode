# Given an array of integers numbers that is sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers (index1, index2), such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]x
#
# Solve with this [1,3,4,5,7,10,11], target = 9 = need to get [3,4]

from email.policy import default
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers approach

        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []
        # Brute Force Method
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return []
        # Binary Search In Python

        for i in range(len(numbers)):
            l, r = i+1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []
        # Hash Table Method

        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i+1]
            mp[numbers[i]] = i + 1
        return []
