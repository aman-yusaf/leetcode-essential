
from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str )-> bool:
        """Return true if t is an ANAGRAM of s, and false otherwise."""
        
        if len(s) != len(t):
            return False
        
        ct1, ct2 = Counter(s),Counter(t)
        if ct1 == ct2 :
            return True
        else:
            return False