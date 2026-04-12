import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s[::-1]
        s=s.replace(" ","")
        t=t.replace(" ","")
        s = s.lower()
        t = t.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        t = re.sub(r'[^a-zA-Z0-9]', '', t)
        if s == t:
            return True
        else:
            return False 
        