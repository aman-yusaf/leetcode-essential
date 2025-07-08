from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(sself, strs: List[str])-> List[List[str]]:
        """ Groups the ANAGRAMS together. """
        
        # To group Anagrams.
        anagram_dic = defaultdict(list)

        for string in strs:
            # Setting the key as sorted string.
            key = ''.join(sorted(string))
            # Appending string as values to list of whose sorted matches the key. 
            anagram_dic[key].append(string)
        # Returning group anagrams as a list.
        return list(anagram_dic.values())