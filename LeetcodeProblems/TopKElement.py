#Given an ineger array nums and an ineger k, return the total number of continuous subarrays whose sum equals to k.
#Example 1:
    #Input: nums = [1,2,2,3,3,3], k = 2
    #Output: [2,3]

class soultion:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # is a dictionary that will store the frequency of each element
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) 1, 0, -1)
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
