class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sstring = list(s)
        tstring = list(t)

        sstring.sort()
        tstring.sort()

        if sstring == tstring:
            return True 
        return False 
        