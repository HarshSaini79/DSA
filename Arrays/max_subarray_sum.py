"""(Kadane's Algorithm)
Statement:
Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""



def maxSubArray(nums):     #defined a function for max SubArray
    max_sum = current_sum = nums[0]   #intitally max and current sum set to 0
    for num in nums[1:]:           #starts iteration from 1st index not 0th
        current_sum = max(num , current_sum+ num) #trying to get max value for current sum at every iteration
        max_sum = max(max_sum , current_sum)        #chooses the maximum sum between current sum or  max sum 
    return max_sum  

print(maxSubArray([-2,3,-4,-5,6,-7,8,-9]))
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
