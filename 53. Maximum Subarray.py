class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = [0] * len(nums)
        sum [0] = nums[0]
        
        for i in range (1, len(nums)):
            sum[i] = max (nums[i], nums[i] + sum[i-1] )
        return max(sum)
