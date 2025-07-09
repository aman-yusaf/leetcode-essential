from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums : List[int], k : int)-> List[int]:
        """ Returns the k most frequent integers. """ 

        # Counter returns the integers : frequency
        frequencyCounter = Counter(nums)

        # If 'k' is greater than all the 'unique integers' present ,We can return all of them.  
        if len(frequencyCounter) <= k :
            return list(frequencyCounter.keys())
        
        # Sorting the counter by frequency to find the most frequent integer and appending to list till k.
        sortedCount = sorted(frequencyCounter.items(),key=lambda item: item[1], reverse=True)
        return [num for num,count in sortedCount[:k]]




    

        

        
        

        


