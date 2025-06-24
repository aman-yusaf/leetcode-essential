# %%
class Solution:
    def two_Sum(self, nums, target):
        """ returns the indices of the 2 numbers such that they add upto target """
        hashmap = {}
        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in hashmap:
                return [hashmap[compliment], index]
            hashmap[num] = index

# %%
