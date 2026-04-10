class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nested=set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        chunk = [nums[i],nums[j],nums[k]]
                        nested.add(tuple(chunk))
        return [list(i) for i in nested]

    