from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        """ Encodes a list of strings to a single string."""
        return ''.join(f'{len(string)}&{string}' for string in strs)

    def decode(self, s: str) -> List[str]:
        """ Decodes the single string back to list of strings. """
        decoded = []
        i = 0
        end = 0 
        while i<len(s):
            # When i == '&' we can get the length of the string, and then use it to slice the substring.
            if s[i]=='&':
                length = int(s[end:i])
                start = i+1
                end = start + length
                decoded.append(s[start:end])
                i = end
            i+=1
        return decoded

            
