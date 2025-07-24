from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int])-> List[int]:
        """Returns an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]."""
        size = len(nums)
        products = [1]*size

        left = 1
        for i in range(size):
            products[i] = left
            left *= nums[i]
        
        right = 1
        for i in reversed(range(size)):
            products[i] *= right
            right *= nums[i]
            
        return products

