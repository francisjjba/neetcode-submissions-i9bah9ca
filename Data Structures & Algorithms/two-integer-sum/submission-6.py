class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if i!=j and num1 + num2 == target:
                    return [i,j]
               

























        '''
        indices = {} #dictionary 

        for i , n in enumerate(nums): #enumerate counter 
            indices[n] = i #add a counter for n value

        for i , n in enumerate(nums): #enumerate counter 
            diff = target - n #check the diff using target - n value 
            if diff in indices and indices[diff]!=i: #check if diff is in indices & diff == i
                return [i,indices[diff]] #return i and qualifying diff 
            return [] #return set '''