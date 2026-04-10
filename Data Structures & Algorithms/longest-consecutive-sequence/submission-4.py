from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        countT = 1      # start at 1 (first element)
        maxCount = 1

        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1]:
                continue          # skip duplicates

            elif nums[i] == nums[i - 1] + 1:
                countT += 1       # consecutive → extend streak

            else:
                maxCount = max(maxCount, countT)
                countT = 1        # reset streak

        return max(maxCount, countT)



'''class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        countT = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    continue
                elif nums[j]==nums[i]+1:
                    countT +=1'''
            
        