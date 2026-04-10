class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "" # if not present in the list 
        sizes, res = [], "" #create empty list sizes to store len of the string element , res empty dict ,
        for s in strs:  # for loop strs for the len of each element 
            sizes.append(len(s)) 
        for sz in sizes: # add the values in the res 
            res += str(sz)
            res += ',' #after addding add a comma ',' in the end 
        res += '#' # and a # after the loop
        for s in strs: #add string with no seperator 
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s: #checkif its empty 
            return []
        sizes, res, i = [], [], 0 #create sizes , res , i- pointer 
        while s[i] != '#': #loop until you find #
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res