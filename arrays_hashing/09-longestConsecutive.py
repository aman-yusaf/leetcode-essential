
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ Returns the length of the longest consecutive sequence of elements that can be formed."""
        num_Set = set(nums)
        longest = 0
        
        for num in num_Set:
            # Start only if it's the beginning of a consecutive sequence. 
            if num-1 not in num_Set:
                length = 1
                que = num
                while que + 1 in num_Set:
                    que += 1
                    length += 1
                longest = max(longest, length)
        
        return longest
