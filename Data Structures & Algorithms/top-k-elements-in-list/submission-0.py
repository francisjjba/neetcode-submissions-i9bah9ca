class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={} #create count 
        for num in nums: # check through the nums 
            count[num] =1 + count.get(num,0)  #start count and add dict key value pair with key and value with repeating values 

        arr =[] #create an array 
        for num, cnt in count.items(): #make the dict in a array inside an array 
            arr.append([cnt,num]) # swap the values with key and values i.e. cnt and num 
        arr.sort() #sort it to asc order 

        res=[]  #create a list res 
        while len(res) < k: #check if the k is equal res 
            res.append(arr.pop()[1])  # pop the element and create a list with the index value of 1 
        return res  # return res