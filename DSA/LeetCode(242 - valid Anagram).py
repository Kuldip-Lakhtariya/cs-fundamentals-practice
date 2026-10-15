# Pattern : Anagram means the word with same letters so I compare the letters, and early stop if the length doesn't match. (Hashmap counting) 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def count_letters(word: str) -> dict[str,int]:
            counts: dict[str,int] = {}
            for ch in word:
                counts[ch] = counts.get(ch,0) +1
            return counts

        return count_letters(s) == count_letters(t)