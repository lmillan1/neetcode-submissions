class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # no duplicattes so we wanna use a set
        char_s = set()
        res = 0
        left = 0
        # string 
        for r in range(len(s)):
            # if there exist a duplicate shrink the window
            while s[r] in char_s:
                char_s.remove(s[left])
                left += 1
            char_s.add(s[r])

            res = max(res, r - left + 1)
        return res