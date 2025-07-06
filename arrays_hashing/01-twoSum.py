from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns the indices of the two numbers such that they add up to the target.
        """
        hashmap = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], index]
            hashmap[num] = index

        # when no favorable solutions found
        return []

