class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count_s = {}

        count_t = {}

        for num in s:
            count_s[num] = count_s.get(num, 0) + 1

        for num in t:
            count_t[num] = count_t.get(num, 0) + 1

        return count_t == count_s
        