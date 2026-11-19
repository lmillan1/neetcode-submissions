class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case: length of the string
        if len(s) != len(t):
            return False 

        s_dict = {}
        t_dict = {}

        # frequency of each string
        for char in s:
            s_dict[char] = s_dict.get(char, 0) +1
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        
        return s_dict == t_dict
        