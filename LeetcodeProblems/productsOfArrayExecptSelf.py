# Given an array nums, return an array output where output[i] is equal to the product of all the elements of nums except nums[i] is the product of all the elements of nums execept nums[i].
# Each Product is guranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Example 1:
    # Input: nums = [1, 2, 3, 4]
    # Output: [24, 12, 8, 6] // `Muiltiply all the elements in the array except the element itself.`
class Soultion:
    def productExecptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1): # going at the end of the array to go backwards
            res[i] *= postfix
            postfix *= nums[i]
        return res
