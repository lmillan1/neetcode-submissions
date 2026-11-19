class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # freq of each char and check if both of the freq
        # are the same 
        if len(s) != len(t):
            return False 
            
        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t 
        


        # sorted_s = "".join(sorted(s))
        # sorted_t = "".join(sorted(t))

        # return sorted_s == sorted_t 