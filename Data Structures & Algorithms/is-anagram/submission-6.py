class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # racecar
        # carrace
        # dictionary, key(character) value:(frequency)
        # same length to be considered an anagram so do that initial check

        if len(s) != len(t):
            return False 

        char_dict_s = {}
        char_dict_t = {}

        for char in s:
            char_dict_s[char] = char_dict_s.get(char, 0) + 1
        for char in t:
            char_dict_t[char] =  char_dict_t.get(char, 0) + 1
        
        return char_dict_s == char_dict_t
        