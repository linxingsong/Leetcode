# Given an integer array nums, find the contiguous subarray (containing at least one number)
#  which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # simple answer
        max_so_far = curr_so_far = -float('inf')
        for i in range(len(nums)):
            curr_so_far += nums[i] # Add curr number
            curr_so_far = max(curr_so_far, nums[i]) # Check if should abandon accumulated value so far if it's a burden due to negative value accumulated
            max_so_far = max(max_so_far, curr_so_far) # Update answer
            
        return max_so_far