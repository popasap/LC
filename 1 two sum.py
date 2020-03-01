class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_given={}
        for i in range(len(nums)):
            if (target-nums[i]) not in dict_given.keys():
                dict_given[nums[i]]=i
            else:
                return [i,dict_given[target-nums[i]]]
