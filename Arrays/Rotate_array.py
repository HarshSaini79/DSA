"""Rotate Array
Statement:
Given an array nums, rotate the array to the right by k steps, where k is non-negative."""

def rotate_array(nums,k):
    k %= len(nums)    #reducing k because if k will be greater than len of array then k will result in wrong slicing of list. 
    nums[:] = nums[-k:] +nums[:-k] #nums [:] = updating existing array for not consuming extra space
    return nums


print(rotate_array([1, 2, 3, 4, 5, 6, 7], 5))
print(rotate_array([1, 2, 3, 4, 5, 6, 7], 8))