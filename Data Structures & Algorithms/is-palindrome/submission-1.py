class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we want to work with a cleaned string

        cleaned_string = "".join(char.lower() for char in s if char.isalnum())

        l, r = 0, len(cleaned_string) - 1

        while l < r:
            # wasitacaroracatisaw
            # w w
            if cleaned_string[l] != cleaned_string[r]:
                return False
            l += 1
            r -= 1

        return True
            
 