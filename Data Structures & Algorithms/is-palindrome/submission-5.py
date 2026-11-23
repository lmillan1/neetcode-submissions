class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join(char.lower() for char in s if char.isalnum())

        left, right = 0, len(cleaned_string) - 1
        
        while left < right:
            if cleaned_string[left] != cleaned_string[right]:
                return False
            left += 1
            right -= 1
        return True 
           

        
        
        