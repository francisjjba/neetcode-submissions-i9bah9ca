#hash maps (two pass)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  #set

        for i , n in enumerate(nums):  #passing values and storing nums in indices indices 
            indices[n] = i 

        for i , n in enumerate(nums): # passing the nums 
            diff = target - n  # find diff between target and i 
            if diff in indices and indices[diff] != i: #check if diff value in indices  and diff not in i
                return [i,indices[diff]] #return value i and diff value 
        return [] # nothing to search, return empty list