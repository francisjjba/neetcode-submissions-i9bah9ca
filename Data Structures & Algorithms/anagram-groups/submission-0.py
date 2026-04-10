class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} #converted to dictionary

        for word in strs:
            key = "".join(sorted(word))  # sorted letters as key

            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        
        return list(anagrams.values())

#convert it to dict 
# sort the word 
# join the sorted 
# 