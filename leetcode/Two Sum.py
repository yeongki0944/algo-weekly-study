class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for i in range(0, len(nums)):
            key = target - nums[i]
            dic[key] = i
    
 
        for i in range(0, len(nums)):
            key = nums[i]
            if key in dic:
                value = dic[key]
                if i!=value :
                    print(i, value)
                    return[i, value]