from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """  Returns true if any value appears at least twice in the array, and return false if every element is distinct. """
        # Simple approach as set doesn't store duplicate elements
        return len(nums) != len(set(nums))

