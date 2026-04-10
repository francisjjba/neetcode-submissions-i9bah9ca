class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp = ''
        for c in s:
            if c.isalnum():
                sp += c.lower()
        return sp==sp[::-1]

        