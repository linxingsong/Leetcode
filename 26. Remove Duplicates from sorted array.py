# 26. Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that
#  each element appear only once and return the new length.

# Do not allocate extra space for another array, 
# you must do this by modifying the 
# input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        
        #2 points, one for loc, one for checking. 
        # Put uniqut one to located point in the array.
        i=1
        for n in range(1, len(nums)):
            if nums[n] != nums[i-1]:
                nums[i]= nums[n]
                i+=1
        return i