class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        maxnum = max(nums)
        diffnums = []
        for i in range(maxnum+1):
            diffnums.append(i)
        result = list(set(diffnums)-set(nums))
        if not result:
            result = maxnum + 1
        else:
            result = result[0]

        return result
        


#create a copy of nums 
# get the last value of the nums 
# append to the complete nums till the max num 
# compare 
# print value that is missing.       