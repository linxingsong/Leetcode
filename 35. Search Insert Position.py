# Given a sorted array and a target value, return the index if the target is found. If not, 
# return the index where it would be if it were inserted in order.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #binary search
        if len(nums) ==0 or target <= nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)

        # defien left and right.
        left, right = 0, len(nums)

        while left < right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid +1
            else: 
                right = mid -1
        
        if target > num[left]: 
            return left+1
        else:
            return left